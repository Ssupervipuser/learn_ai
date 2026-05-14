import os

from utils import get_llm_client

client = get_llm_client()

# - 链式提示：将复杂任务拆分为多个步骤，每一步的输出作为下一步的输入。
# - 思维链（CoT）推理：要求模型在给出最终答案前，先展示分步推理过程。
# - 自我一致性：在模型给出不确定答案时，通过多次采样并多数投票提高回答的准确性。
#
# 该系统模拟了一个电商平台的客服场景，支持退货、物流查询、产品咨询等常见意图。


# ============================
# 模拟知识库   实际项目中这些数据可能来自于向量数据库 文档检索
knowledge_base = {
    "退货规则": "退货需在签收后7天内申请，商品需保持原包装完好。请提供订单号，我们将为您发起退货流程。",
    "物流查询规则": "请提供运单号，我们将查询最新的物流状态。通常配送时间为3-5个工作日。",
    "产品咨询规则": "感谢您的咨询！请详细描述您想了解的产品功能或规格，我们立即为您解答。"
}

# ============================
# 第一步: 意图识别+实体抽取
# ============================

# intent（字符串）：取值应为 "退货"、"物流查询"、"产品咨询" 或 "其他"。
# entities（对象）：包含该意图可能涉及的关键实体，如 {"订单号": "A123456", "商品": "耳机"}。若某实体未出现，值填 "无"。

def get_intent_entity(user_query):
    """
    分析用户消息，识别其意图（如“退货”），并提取关键实体（如订单号、商品名称）
    :param user_query:
    :return:
    """
    # 返回是处理好的json格式  详情参考文档
    assistant_prompt = """
    你是一个专门处理意图识别的大模型，你需要对输入的文本进行意图识别并返回一个 JSON 对象，至少包含两个字段：

    - intent（字符串）：取值应为 "退货"、"物流查询"、"产品咨询" 或 "其他"。
    - entities（对象）：包含该意图可能涉及的关键实体，如 {"订单号": "A123456", "商品": "耳机"}。若某实体未出现，值填 "无"。
    正确输出结果样本如下：
    {
      "intent": "退货",
      "entities": {
        "订单号": "A123456",
        "商品": "耳机"
      }
    }
    """

    def call_model(prompt):
        result = client.chat.completions.create(
            model=os.getenv("model_name"),
            messages=[
                {"role": "user", "content": f"用户提问：{prompt}"},
                {"role": "assistant", "content": assistant_prompt}
            ]
        )
        return result.choices[0].message.content
    result=call_model(user_query)

    return result


# ============================
# 第二步: 根据意图检索知识库中的规则
# ============================

def search_rule(intent):
    """
    根据识别到的意图，从预定义的知识库（或未来的数据库/文档库）中获取相关的业务规则或话术模板。
    :param intent:
    :return:
    """

    return knowledge_base.get(intent + "规则", "抱歉,我暂时无法处理您的问题")


# ============================
# 第三步: 使用COT生成问题 ,如果模型不确定,启动自我一致性
# ============================
def generate_answer_with_self_Consistency(user_query, rule, entities):
    """
        综合生成最终客服回答:
            1:先用提示词要求模型一步一步思考+给出答案 ,并让模型自己判断答案是否确定
            2:如果模型标记  #确定 ,直接采用这个答案  返回函数
            3:如果模型标记  #不确定,则启动自我一致性
                规则: 少数服从多数  投票
        :param user_query:
        :param rule:
        :param entities:
        :return:
        """
    # 构建提示词
    base_prompt = f"""
                你是客服助手,参考一下规则回答用户问题
                规则:{rule}
                用户问题:{user_query}
                提取的实体:{entities}
                请先逐步推理,然后给出最终答案,在答案的最后一行,附上你的确定性评价: '#确定' 或 '#不确定'
    """
    # 调用大模型
    resp = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[{"role": "user", "content": base_prompt}]
    )
    first_model_result = resp.choices[0].message.content

    if "#确定" in first_model_result:
        return first_model_result.replace("#确定", "").strip()

    # 如果代码走到这里 ,说明启动自我一致性(5次)
    print("自我一致性启动")
    #用一个字典容器来记录某个回答文本,->出现次数 ,手动实现投票
    final_dict={}

    for i in range(5):
        result = client.chat.completions.create(
            model=os.getenv("model_name"),
            messages=[{"role": "user", "content": base_prompt}]
        )
        f_result=result.choices[0].message.content

        #如果字典里面还有没有回答这个问题,就初始化为0,然后+1
        final_dict[f_result]=final_dict.get(f_result,0)+1

    #找票数最多的
    best_result=max(final_dict,key=final_dict.get)
    print("投票产生最佳回复")
    return best_result



# ============================
# 主流程
# ============================

def main_service(user_query):
    """
    1:意图识别+提取实体
    2:根据意图检索知识库
    3:用Cot+自我一致性生产最终回答
    :param user_query:
    :return:
    """
    # """{
    #        "intent": "退货",
    #        "entities": {
    #            "订单号": "A123456",
    #            "商品": "耳机"
    #        }
    #    }"""
    result=get_intent_entity(user_query)
    print(f"第一步执行：{result}")

    info = eval(result) #dict
    print(f"info:{info}")
    # print(type(result))

    rule=info["intent"]
    print(f"rule:{rule}")

    search_rule_result=search_rule(rule)
    final_answer=generate_answer_with_self_Consistency(user_query,info,rule)
    print(final_answer)
    return final_answer

# ============================
# 程序入口
# ============================
if __name__ == '__main__':
    test_query = "我买了耳机到货三天,但是我想退货,订单号是A123456"
    main_service(test_query)



    # result = """{
    #        "intent": "退货",
    #        "entities": {
    #            "订单号": "A123456",
    #            "商品": "耳机"
    #        }
    #    }"""
    # result = eval(result) #dict
    # # print(result)
    # # print(type(result))
    #
    # intent=result["intent"]
    # print(intent)
    # search_rule(intent)



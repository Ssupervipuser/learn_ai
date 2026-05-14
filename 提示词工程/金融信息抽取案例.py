import json
import os

# todo 1  导包
from utils import get_llm_client

client = get_llm_client()



# todo 2few_shot 定义信息抽取任务示例数据  供模型学习
ie_examples = [
    {
        'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
        'answers': {
            '日期': ['2023-01-10'],
            '股票名称': ['古哥-D[EOOE]美股'],
            '开盘价': ['100美元'],
            '收盘价': ['102美元'],
            '成交量': ['520000'],
        }
    }
]


# todo 3 构建系统提示词 ,定义AI角色与抽取规则
system_prompt = f"""
        你是一个专业金融信息领域抽取专家,需要完成信息抽取任务,
        我会给你一个句子,需要抽取句子中的日期,股票名称,开盘价,收盘价,成交量.
        输出格式必须为严格JSON格式,不存在的信息用['原文中未提及']表示,禁止输出多余的内容
"""

# todo 4 构建消息上下文 ,注入系统提示词和示例数据
messages = [
    {"role": "system", "content": system_prompt}
]

for exa in ie_examples:
    messages.append({"role": "user", "content": exa['content']})
    messages.append({"role": "assistant", "content": json.dumps(exa['answers'], ensure_ascii=False)})
# print(messages)


# todo 5 待抽取的文本
sentences = [
    '2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
    '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
]


# todo 6 调用大模型
def call_qwen(promot):
    model_result = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=messages + [{"role": "user", "content": f"现在请完成:{promot}"}]

    )
    return model_result.choices[0].message.content

# todo 7 .批量处理
for  question in sentences:
    # model_result=call_qwen(question)

    print(f"用户问题:{question}")
    # print(f"模式输出:{model_result}")
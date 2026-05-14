# 基于 ReAct 范式实现的天气小助手，核心功能是响应用户的天气相关查询问题，可自主调用工具补全信息并返回完整的天气结果。
# 处理流程：
# 当用户问："今天天气怎么样？"
# 系统会：
# 思考：要回答今天的天气，首先需要获取当前的准确日期行动：调用 get_current_date 获取当前日期观察：得到 "2026-05-08
# 思考：用户未说明查询的城市，需要获取用户所在地行动：调用 get_user_location 获取用户所在城市观察：得到 "南京"
# 思考：已获取到查询所需的城市和日期，需要调取对应天气信息行动：调用 get_weather ("南京","2026-05-08")观察：得到 "南京，2026-05-08，天气：晴天；气温：25℃；空气湿度：50%；AQI：11"
# 思考：已获取完整的天气信息，可以输出最终答案最终回答：2026 年 05 月 08 日，南京天气为晴天，气温 25℃，空气湿度 50%，空气质量 AQI 11，整体天气晴好。
import os
import random
# 1.导包
from datetime import datetime
from openai import OpenAI
from utils import get_llm_client

client = get_llm_client()

# 2.写工具
# 工具1: 获取当前日期  年月日
def get_current_date():
    return f"{datetime.now()}"


# 工具2:获取用户位置
def get_user_location():
    return random.choice(['郑州', '南京', '北京', '洛阳', '开封'])

# 工具3:获取天气
def get_weather(city, date):
    return f"{city},{date},天气:晴天,气温:25℃,空气湿度:70%"

#3.注册工具
TOOLS={
    "get_current_date":get_current_date,
    "get_user_location":get_user_location,
    "get_weather":get_weather
}

#4.调用千问模型
def call_qwen(prompt):
    result=client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[
            {"role":"user","content":prompt}]
    )
    return result.choices[0].message.content

#5.解析模型返回
def parse_model_output(mode_result:str):
    """
    从模型输出中解析
    thought,
    aciton
    action_input
    :param mode_result:
    :return:
    """

    # Thought: 为了回答关于今天天气如何的问题，我首先需要知道用户所在的位置。由于当前上下文没有提供用户的地理位置信息，因此我的第一步应该是获取这个信息。
    # Action: get_user_location
    # Action Input: ""
    lines=mode_result.split("\n")
    for line in lines:
        line=line.strip()
        if line.startswith("Thought:"):
            thought=line.replace("Thought:","").strip()
        elif line.startswith("Action:"):
            action=line.replace("Action:","").strip()
        elif line.startswith("Action Input:"):
            action_input=line.replace("Action Input:","").strip()
    return thought,action,action_input

#6.react方法
def react(question):
    """
    react主流处理函数: 思考->行动->观察  迭代  ->最终答案
    :param question:用户提出问题  eg: 今天天气如何?
    :return:最终天气答案
    """
    # 存储每一轮的思考,动作,工具结果,作为上下文给模型
    steps=[]
    max_count=5
    context="" #上下文
    for i in range(1,max_count+1):
        print(f"第{i}次调用大模型")
        #context=""
        #拼接上下文,把之前的思考,动作,工具拼接到一起
        for step in steps:
            context+= step+"\n"
        print(f"-------历史上下文开始\n{context}------历史上下文结束")

        #编写提示词
        prompt=f"""
                你是一个使用ReAct范式的智能代理,必须严格按照以下格式进行输出:
                [输出格式(必须一字不差的遵守)]
                Thought:<你的思考过程>
                Action:<只能从['get_current_date','get_user_location','get_weather']中选择,或在确定答案后填写 Final Answer>
                Action Input:<如果Action是动作名称,则填写该工具的输入参数;如果Action是Final Answer，则填写最终的答案>要求必须是字符串格式
                当前上下文:
                {context}
                问题:{question}
                [核心规则]
                - 如果未知用户所在的城市,需要调用get_user_location
                - 如果未知日期,需要调用get_current_date
                - 必须先调用城市,在调用日期
                - 如果需要天气,调用get_weather
                - 信息足够,返回Final Answer
                [正确输出样本]
                思考:已获取用户所在城市为洛阳，具体日期为2026-05-08。根据核心规则与执行顺序，已满足查询天气的前置条件，下一步需调用get_weather工具获取今日天气数据。
                行动:get_weather
                行动输出:洛阳,2026-05-08
        """
        model_result=call_qwen(prompt)
        thought,action,action_input=parse_model_output(model_result)
        print("*"*20)
        print(f"思考:{thought}")
        print(f"行动:{action}")
        print(f"行动输出:{action_input}")

        #增加代码健壮性
        if not thought and not action:
            print("解析失败,继续下一轮")
            continue

        steps.append(f"思考:{thought}")
        steps.append(f"动作:{action}")

        #代码结束标志
        if action == "Final Answer":
            print("流程结束,最终结果:")
            print(action_input)
            return action_input

        #===============调用工具===============
        #['get_current_date','get_user_location','get_weather']
        if action in TOOLS:
            if action=="get_current_date":
                tool_result=get_current_date()
            elif action =="get_user_location":
                tool_result=get_user_location()
            elif action=='get_weather':
                print(action_input)
                city=action_input.split(",")[0].strip()
                date = action_input.split(",")[1].strip()
                tool_result=get_weather(city,date)
            steps.append(f"调用结果:{tool_result}")
        else:
            print(f"模型要求的工具:{action}不存在,跳过")
            continue

if __name__ == '__main__':
    # print(get_current_date())
    # print(get_user_location())
    # print(get_weather("杭州","2026-05-08"))
    react("今天天气如何?")
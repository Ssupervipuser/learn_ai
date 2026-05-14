import os
import random
from datetime import datetime

from utils import get_llm_client
from openai import OpenAI

client = get_llm_client()


# 定义工具
def get_current_date():
    return f"{datetime.now()}"


def get_user_location():
    return random.choice(['郑州', '南京', '北京', '上海'])


def get_weather(city, date):
    return (f"{city},{date},天气请，气温25℃，空气湿度70%")


# 工具注册
TOOLS = {
    "get_current_date": get_current_date,
    "get_user_location": get_user_location,
    "get_weather": get_weather
}


# 封装调用模型
def call_qwen(prompt):
    result = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return result.choices[0].message.content


def parse_model_output(model_result: str):
    lines = model_result.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("Thought:"):
            thought = line.replace("Thought:", "").strip()
        elif line.startswith("Action:"):
            action = line.replace("Action:", "").strip()
        elif line.startswith("Action Input:"):
            action_input = line.replace("Action Input:", "").strip()
    return thought, action, action_input


def react(question):
    # 存储每一轮的思考，动作，工具结果，作为上下文给模型
    steps = []
    max_count = 5
    context = ""
    for i in range(1, max_count + 1):
        print(f"第{i}次调用大模型")
        for step in steps:
            context += step + "\n"
        print(f"--------历史上下文\n{context}--------历史上下文end")

        prompt = f"""
                你是一个使用ReAct范式的智能代理，必须严格按照以下格式输出:
                  [输出格式(必须一字不差的遵守)]
                  Thought:<你的思考过程>
                  Action:<只能从["get_current_date","get_user_location","get_weather"]中选择，或则确定的答案后写Final Answer>
                  Action Input:<如果Action是动作的名称，则填写该工具的输入参数，如果Action是Final Answer，则填写最终答案>
                  
                  当前上下文：
                  {context}
                  
                  问题：{question}
                  [核心规则]
                  get_weather这个工具必须是最后一个调用
                  [正确输出样本]
                思考:已获取用户所在城市为洛阳，具体日期为2026-05-08。根据核心规则与执行顺序，已满足查询天气的前置条件，下一步需调用get_weather工具获取今日天气数据。
                行动:get_weather
                行动输出:洛阳,2026-05-08
        """
        # 调用模型
        model_result = call_qwen(prompt)

        thought, action, action_input = parse_model_output(model_result)
        print("*jiexi"*20)
        print(f"思考:{thought}")
        print(f"行动:{action}")
        print(f"行动输出:{action_input}")


        # 模型解析判断增加健壮性
        if not thought and not action:
            print("解析失败，继续尝试")
            continue
        steps.append(f"Thought:{thought}")
        steps.append(f"Action:{action}")

        if action == "Final Answer":
            print("最终答案")
            print(action_input)
            return action_input

            # 执行工具
        if action in TOOLS:
            if action == "get_current_date":
                tool_result=TOOLS[action]()

            elif action=="get_user_location":
                tool_result=TOOLS[action]()

            elif action=="get_weather":
                print("actioninputlllll",action_input)
                city=action_input.split(",")[0].strip()
                date=action_input.split(",")[1].strip()

                tool_result=TOOLS[action](city, date),
            steps.append(f"调用结果：{tool_result}")
        else:
            print(f"模型要求的工具：{action}不存在")
            continue



if __name__ == '__main__':
    # date=(get_current_date())
    # print(date)
    # loc=(get_user_location())
    # print(loc)
    # print(get_weather(loc, date))

    react("今天天气如何？")

    # model_result="""
    # Thought:用户询问今天天气如何。为了准确查询天气信息，我需要先确认“今天”的具体日期。同时根据核心规则，get_weather必须是最后一个调用的工具，因此我第一步先调用获取当前日期的工具。
    # Action: get_current_date
    # Action Input: {}
    # """
    # def parse_model_output(model_result: str):
    #     lines = model_result.split("\n")
    #     lines = model_result
    #     for line in lines:
    #         print("line",line)
    #
    # parse_model_output(model_result)
    # action="get_current_date"
    # if action in TOOLS:
    #     if action == "get_current_date":
    #         result = TOOLS[action]()
    #         print(result)
    #
    #     elif action == "get_user_location":
    #         result = TOOLS[action]()
    #         print(result)
    #     elif action == "get_weather":
    #         # city = action_input.split(",")[0].strip()
    #         # date = action_input.split(",")[1].strip()
    #
    #         result = TOOLS[action](city, date),
    #     else:
    #         print(f"模型要求的工具：{action}不存在")

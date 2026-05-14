import os
import random
from datetime import datetime

from utils import get_llm_client
from openai import OpenAI

client = get_llm_client()


# 1. 定义工具获取当前日期（如用户未指定日期，则通过这个函数获取当天日期，用于支撑用户提到的明天、后天等信息）
def get_current_date():
    # return f"{datetime.now()}"
    return datetime.now().strftime("%Y-%m-%d")


# 2. 定义工具获取用户所在地（如用户未提供出发地，则用这个函数获取城市作为出发地）
def get_user_location():
    return random.choice(['郑州', '南京', '北京', '上海'])


# 3. 定义工具查询车票（传入出发地、目的地、日期）返回车票信息（内容随意编造即可）

def get_query_ticket(form_city, target, date):
    return f"{date}从{form_city}到{target}地方目前有票"


# 注册工具
TOOLS = {
    "get_current_date": get_current_date,
    "get_user_location": get_user_location,
    "get_query_ticket": get_query_ticket
}


def call_model(prompt):
    result = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[
            {
                "role": "user", "content": prompt
            }
        ]
    )
    return result.choices[0].message.content


# 解析模型输出
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
    steps = []
    max_count = 5
    context = ""
    for i in range(1, max_count + 1):

        for step in steps:
            context += step + "\n"

        prompt = f"""
                你是一个使用ReAct范式的智能代理，必须严格按照以下格式输出:
                  [输出格式(必须一字不差的遵守)]
                  Thought:<你的思考过程>
                  Action:<只能从["get_current_date","get_user_location","get_query_ticket"]中选择，或则确定的答案后写Final Answer>
                  Action Input:<如果Action是动作的名称，则填写该工具的输入参数，如果Action是Final Answer，则填写最终答案>
                  
                  当前上下文：
                  {context}
                  
                  问题：{question}

        """
        print(f"模型的第{i}次调用")
        model_result = call_model(prompt)
        print(model_result)
        thought, action, action_input = parse_model_output(model_result)
        print(f"解析|thought：{thought}")
        print(f"解析|action：{action}")
        print(f"解析|action_input：{action_input}")

        # 开始判断解析结果
        if not thought and not action:
            print("解析失败，继续尝试")
            continue

        steps.append(f"Thought:{thought}")
        steps.append(f"Action:{action}")

        if action == "Final Answer":
            print("任务完成，最终答案：")
            print(action_input)
            return action_input

        if action in TOOLS:
            if action == "get_current_date":
                tool_result = get_current_date()

            elif action == "get_user_location":
                tool_result = get_user_location()

            elif action == 'get_query_ticket':
                print("action_inputzzzz",action_input)
                form_city = action_input.split(",")[0].strip()
                target = action_input.split(",")[1].strip()
                date = action_input.split(",")[2].strip()
                tool_result = get_query_ticket(form_city, target,date)
            steps.append(f"调用结果:{tool_result}")
        else:
            print(f"模型要求的工具:{action}不存在,跳过")
            continue


if __name__ == '__main__':
    # date=(get_current_date())
    # print(date)
    # loc=(get_user_location())
    # print(loc)
    # print(get_query_ticket(loc,"上海", date))
    #
    react("帮我查一查，明天去上海的车票")

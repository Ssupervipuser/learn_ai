# 1：导包
import os
from datetime import datetime

from openai import OpenAI
from utils import get_llm_client

client = get_llm_client()


# 2:创建工具类
# 2-1获取当前日期
def get_current_date():
    return f"{datetime.now().month}月"


def search_holidays(month):
    """
     查询指定月份的法定节假日
     month: 月份字符串，如 "9月"
     """
    # 模拟节假日数据
    holidays = {
        "1月": ["元旦：1月1日"],
        "2月": ["春节：1月28日-2月3日"],
        "3月": [],
        "4月": ["清明节：4月4日-6日"],
        "5月": ["劳动节：5月1日-5日", "端午节：5月31日-6月2日"],
        "6月": [],
        "7月": [],
        "8月": [],
        "9月": [],  # 2025年9月没有法定节假日
        "10月": ["中秋节：10月6日-8日", "国庆节：10月1日-7日"],
        "11月": [],
        "12月": ["元旦：12月31日"]
    }
    # 获取对应月份的节假日类别
    #          参1: 传递月份   参2:没有找到返回空列表 []
    holidays_list = holidays.get(month, [])
    if holidays_list:
        return f"2025年{month}有以下法定节假日:\n" + "\n".join(holidays_list)
    else:
        return f"2025年{month}没有法定节假日"


# 3. 注册中心(容器_字典) : 将可以使用的工具放置到字典里
TOOLS = {
    "get_current_date": get_current_date,
    "search_holidays": search_holidays
}


# 4.调用千问模型
def call_qwen(prompt):
    result = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[{"role": "user", "content": prompt}]
    )
    return result.choices[0].message.content


# 5.解析模式输出 (必须有输出)
def parse_model_output(model_result):
    """
    模型结果解析:
    现状:
    Thought:为了回答这个问题，我首先需要知道当前的月份和年份，然后查询这个月有哪些法定节假日。
    Action:get_current_date
    Action Input:
    目标:thought  action  action_input

    :param model_result:
    :return:
    """
    # 按行切分
    lines = model_result.split("\n")
    for line in lines:
        line = line.strip()  # 去除前后空格,换行符
        # Thought:为了回答这个问题，我首先需要知道当前的月份和年份，然后查询这个月有哪些法定节假日。
        if line.startswith("Thought:"):
            # 为了回答这个问题，我首先需要知道当前的月份和年份，然后查询这个月有哪些法定节假日。
            thought = line.replace("Thought:", "").strip()
        elif line.startswith("Action:"):
            action = line.replace("Action:", "").strip()
        elif line.startswith("Action Input:"):
            action_input = line.replace("Action Input:", "").strip()
    return thought, action, action_input


# 6.ReAct 流程
def react(question):
    # # 获取上一步的内容
    steps = []  # 步数
    context = ""  # 内容
    for i in range(1, 6):
        for step in steps:
            context += step + "\n"
        # 2.1 构建提示词
        prompt = f"""
                你是一个使用ReAct范式的智能代理,必须严格按照以下格式输出:
                [输出格式(必须一字不差的遵守)]
                Thought:<你的思考过程>
                Action:<只能从['get_current_date','search_holidays']中选择,或在确定的答案后写 Final Answer>
                Action Input:<如果Action是动作的名称,则填写该工具的输入参数,如果Action是Final Answer，则填写最终答案>
                
                当前上下文:
                {context}
                
                问题:{question}
                """

        print("-" * 80)
        print(f"模型的第{i}次调用")
        print(f"提示词-----{prompt}-----提示词")

        # 2.2调用模型
        model_result = call_qwen(prompt)
        print(f"模型输出:----\n{model_result}\n--模型输出结束")
        thought, action, action_input = parse_model_output(model_result)
        print(f"解析|thought：{thought}")
        print(f"解析|action：{action}")
        print(f"解析|action_input：{action_input}")

        # 2.3模型解析判断
        if not thought and not action:
            print(f"解析失败,继续尝试")
            continue

        steps.append(f"Thought:{thought}")
        steps.append(f"Action:{action}")

        # 2.4如果是最终步骤
        if action == "Final Answer":
            print("任务完成,最终答案:")
            print(action_input)
            return action_input

        # 2.5执行工具
        # "search_holidays": search_holidays"""
        if action in TOOLS:
            if action == "get_current_date":
                result = TOOLS[action]()
            else:
                result = TOOLS[action](action_input)
            steps.append(f"Action Input:{action_input}")
            steps.append(f"Observation:{result}")
        else:
            result = f"无效动作:{action}"
            steps.append(f"Action Input:{action_input}")
            steps.append(f"Observation:{result}")


if __name__ == '__main__':
    react("这个月有几个法定节假日,分别是什么?")

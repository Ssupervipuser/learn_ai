import json
import os

# todo 1  导包
from utils import get_llm_client

client = get_llm_client()

# 金融文本匹配：判断两个金融文本是否类似。


# 1.('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
# 2.('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
# 3.('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),

# todo 2few_shot 定义信息抽取任务示例数据  供模型学习
examples = {
    '是': [
        ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
    ],
    '不是': [
        ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
        ('央行降息，刺激经济增长。', '新能源技术的创新。')
    ]
}

# todo 3 构建系统提示词 ,定义AI角色与匹配规则
system_prompt = f"""
        你是一个专业金融信息领域文本匹配专家,需要完成文本相似度匹配任务,
        我会给你两个句子,需要判断他们之间是否有关系，回答'相似',还是'不相似'.
        不存在的信息用['原文中未提及']表示,禁止输出多余的内容
"""


messages = [
    {"role": "system", "content": system_prompt}
]
# 循环添加用户示例+助手示例答案,让模型学习抽取规则
for key in examples:
    value=examples[key]
    print(value)
    print(type(value))
    for temp in value:
        # print(tmp)
        messages.append({"role": "user", "content": f"句子1:[{temp[0]}],句子2:[{temp[1]}]"})
        messages.append({"role": "assistant", "content": key})

# print(messages)


# todo 5 待抽取的文本
sentences = [
    ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
    ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
    ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
]

# todo 6 调用大模型


def call_qwen(promot):
    model_result = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=messages + [{"role": "user", "content": f"现在请完成:{promot}"}]

    )
    print(f"messages:{messages}")
    return model_result.choices[0].message.content


# todo 7 .批量处理
for  question in sentences:
    model_result=call_qwen(question)

    print(f"用户问题:{question}")
    print(f"模式输出:{model_result}")


if __name__ == '__main__':
    pass

# value=[('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。')]
# print(value[0])
# for tmp in value:
#     print(tmp)
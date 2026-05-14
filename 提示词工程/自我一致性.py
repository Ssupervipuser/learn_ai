"""
需求:
    1:同一个数学问题,生成3种不同的解题思路
    2:根据每种解题思路分别调用大模型计算出答案
    3:对多个答案进行投票,选出出现次数最多的答案,作为最终的答案
    核心目的: 多条路径推理+投票机制 ,提高答案准确性
"""

import dashscope  # 千问SDK
import os
from dotenv import load_dotenv

load_dotenv()


# 2.封装大模型调用函数
def call_llm(prompt):
    response = dashscope.Generation.call(
        model=os.getenv("model_name"),
        api_key=os.getenv("api_key"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # print(response)
    return response.output.text
#3.生成3种解题不同思路
question="一个商店卖铅笔，每支2元。如果小明有20元，他最多能买多少支铅笔？"

step1_prompt=f"""
                你是一个数学老师。请用3种不同的方法来推理这个问题，只需给出推理思路，不需要解答。思路需要简洁明了，并且合理有效。
                输出格式为：["思路1","思路2","思路3"]
                问题如下：
                {question}
"""

#4.调用大模型获取3种思路列表
solution_list=call_llm(step1_prompt)
# print(f"solution_list:{solution_list}")  #[思路1:xxxx,思路2:xxxx]
# print("*"*50)

#5.根据不同的思路分别调用大模型计算
step2_result_list=[]  #存储每次计算出来的结果
for  solution  in eval(solution_list):
    # print(solution)
    step2_prompt=f"""
    你是一个数学老师。请用如下的思路来解决这个问题。只输出答案即可。
                    思路：
                    {solution}
                    问题:
                    {question}
    """

    #调用大模型
    step2_result=call_llm(step2_prompt)
    step2_result_list.append(step2_result)
print(f"step2_result_list：{step2_result_list}")


#6.投票
step3_prompt=f"""
                你是一个公正的投票专家，能够根据用户输入的list格式的多个答案进行投票，哪个答案出现的次数最多
                你就返回哪个答案，需要注意，返回的答案只需要有计算结果就行，不要有过程。
                用户输入的多个答案：
                {step2_result_list}
"""

step3_result=call_llm(step3_prompt)
print("*"*50)
print(f"最终的答案:{step3_result}")

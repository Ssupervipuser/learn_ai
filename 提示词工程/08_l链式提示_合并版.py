import os

from openai import completions

from utils import get_llm_client

client = get_llm_client()

# 定义链式提示 3个系统角色命令提示词
system_prompts = [
    "你是一个信息抽取专家。请从下面的\"\"\"中提取出关键要点，包括：研究背景、研究方法、研究结果、结论。",
    "你是一个学术写作专家。请根据以下\"\"\"，包含的文本中的要点,生成一段逻辑清晰的学术摘要草稿。",
    "你是一个学术语言优化专家。请将以下\"\"\"，使其更加简洁、正式且符合学术论文摘要的风格"
]

# 第一步:原始文本
user_querys = [
    "\"\"\"近年来，深度学习在自然语言处理中的应用取得了突破性进展。本文提出了一种基于注意力机制的改进模型，并在文本分类任务中进行实验。实验结果表明，该方法相比传统方法提高了5%的准确率。研究结论显示，注意力机制能够显著提升模型的表达能力。\"\"\"",
    "",
    ""
]

for i in range(3):
    completions = client.chat.completions.create(
        model=os.getenv("model_name"),
        messages=[
            {"role": "system", "content": system_prompts[i]},
            {"role": "user", "content": user_querys[i]}
        ]
    )
    if i < 2:
        user_querys[i + 1] = f"\"\"\"{completions.choices[0].message.content}\"\"\""

    print(f"提问:{system_prompts[i]}\n{user_querys[i]}")
    print(f"回答:{completions.choices[0].message.content}")

'''
第一次query1
if i<2
第二次query2=result1
第三次query3=result2
'''

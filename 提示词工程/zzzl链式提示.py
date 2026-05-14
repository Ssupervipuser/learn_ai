from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import get_llm_client

client=get_llm_client()

load_dotenv()

o_text = """近年来，深度学习在自然语言处理中的应用取得了突破性进展。本文提出了一种基于注意力机制的改进模型，并在文本分类任务中进行实验。实验结果表明，该方法相比传统方法提高了5%的准确率。研究结论显示，注意力机制能够显著提升模型的表达能力。"""

# ==========第一步:信息抽取专家==========
print("=" * 50)
print("[第一步:信息抽取专家]")

completions1=client.chat.completions.create(
    model=os.getenv("model_name"),
    messages=[
        {"role": "system",
         "content": "你是一个信息抽取专家。请从下面的\"\"\"中提取出关键要点，包括：研究背景、研究方法、研究结果、结论。"},
        {"role": "user", "content": f"""{o_text}"""},
    ]
)
result1=completions1.choices[0].message.content

print("=" * 50)
print("[第二步:学术写作专家]")

completions2=client.chat.completions.create(
    model=os.getenv("model_name"),
    messages=[
        {"role": "system",
         "content": "你是一个信息抽取专家。请从下面的\"\"\"中提取出关键要点，包括：研究背景、研究方法、研究结果、结论。"},
        {"role": "user", "content": f"""{result1}"""},
    ]
)
result2=completions2.choices[0].message.content

print("=" * 50)
print("[第三步:语言优化专家]")



completions3=client.chat.completions.create(
    model=os.getenv("model_name"),
    messages=[
        {"role": "system",
         "content": "你是一个信息抽取专家。请从下面的\"\"\"中提取出关键要点，包括：研究背景、研究方法、研究结果、结论。"},
        {"role": "user", "content": f"""{result2}"""},
    ]
)
result=completions3.choices[0].message.content
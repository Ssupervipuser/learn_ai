import os
from dashscope import Generation
import dashscope

messages = [
    {'role': 'system', 'content': '你是迪迦奥特曼'},
    {'role': 'user', 'content': '你是谁？'}
]
response = Generation.call(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key = "sk-xxx",
    api_key="sk-ca52ba000c2d48ce87510caf7849c8fd",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",  # 模型列表：https://help.aliyun.com/model-studio/getting-started/models
    messages=messages,
    result_format="message"
)
print(response)
#
# if response.status_code == 200:
#     print(response.output.choices[0].message.content)
# else:
#     print(f"HTTP返回码：{response.status_code}")
#     print(f"错误码：{response.code}")
#     print(f"错误信息：{response.message}")
#     print("请参考文档：https://help.aliyun.com/model-studio/developer-reference/error-code")

# 1.导包
import ollama

# 2.创建客户端对象
ol = ollama.Client(host="http://127.0.0.1:11434")

# 3.发送请求获取响应
response = ol.chat(
    model="qwen2.5:7b",
    messages=[
        {"role": "user", "content": "你是谁"}
    ]
)
# 4.解析响应结果，并输出
# content = response.message.content
content = response['message']['content']
print(content)
# todo 需要先启动ollama
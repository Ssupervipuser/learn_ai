import ollama
#2.创建客户端对象
ol=ollama.Client(host="http://127.0.0.1:11434")

#3.发送给请求获取响应
response=ol.chat(
    model="deepseek-r1:1.5b",

    messages=[
        {
            "role":"user",
            "content":"你好"
        }
    ]
)

#4.解析响应结果，并输出
#content=response.message.content
content=response['messages']['content']
print(content)

# import ollama
#
#
# ol = ollama.Client(host="http://127.0.0.1:11434")
#
# response = ol.chat(
#     model="deepseek-r1:1.5b",
#     messages=[
#         {"role": "user", "content": "给我讲个笑话"}
#     ]
# )
#
#
#
# # content = response.message.content
# content = response['message']['content']
# print(content)

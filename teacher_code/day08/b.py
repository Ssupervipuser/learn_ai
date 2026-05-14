# 后台程序: 用于连接ollama服务 获取大模型响应的结果
# 1- 导入ollama的库
import ollama

# 2- 定义一个函数: 接收用户输入的提示词, 返回响应的结果信息
def chat_message(prompt, model='qwen2:0.5b'):
    try:
        # 2.1 创建ollama的客户端
        client = ollama.Client(host='http://127.0.0.1:11434')

        # 2.2 发起聊天操作
        response = client.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': prompt  # 用户提问
            }]
        )

        # 2.3 获取结果
        print(response)
        # assistant_content = response.message.content

        assistant_content = response['message']['content']

        return assistant_content

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print(e)
        return "服务器繁忙，请重新访问"


if __name__ == '__main__':
    # 测试
    print(chat_message('说话！'))
    prompt = '再说一句！'
    ret = chat_message(prompt)
    print(ret)
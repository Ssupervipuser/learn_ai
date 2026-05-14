import streamlit as st
from ai_backend import chat_message

st.title('黑马聊天机器人') # 页面标题

st.divider() # 分割线

# ============ 实现 历史对话消息列表 ===========
# todo messages是固定写法、streamlit框架规定的
# todo st.session_state保存所有消息
# todo st.session_state['messages'] 专门保存对话消息
if 'messages' not in st.session_state:
    # 如果st.session_state没有messages这个key 那就说明：
    # 1. 没有历史对话消息
    # 2. 需要创建新的messages空列表用来存储历史对话消息
    # 3. st.session_state[key] = value
    st.session_state['messages'] = []

    # todo 把机器人的消息添加到列表中
    st.session_state['messages'].append(
        {
            'role': 'assistant', # 角色
            'message': '你好！我是黑马智聊机器人，请问有什么可以帮你的吗？'
        }
    )

# ==================遍历输出消息列表中每一个角色和其说的话====================
# 遍历st.session_state['messages']中的每一个对话内容字典
for message_dict in st.session_state['messages']:
    # 展示一个对话消息，message_dict['role']是角色
    # message_dict['message'] 就是该角色所说的话
    st.chat_message(message_dict['role']).write(message_dict['message'])


# =================接收用户输入、并展示，添加到消息列表中==================
# =================机器人回答问题，并把机器人的回答添加列表中==================
# 让用户输入 输入框
user_content = st.chat_input('请输入问题：')

# 用户只要输入信息，就把用户输入添加到 st.session_state['messages'] 历史对话列表中
if user_content:
    # todo把用户刚刚的输入的内容立刻展示
    st.chat_message('user').write(user_content)
    # todo 把用户的输入添加到列表中
    st.session_state['messages'].append(
        {
            'role': 'user', # 角色
            'message': user_content # 用户输入的内容
        }
    )

    # todo 通过ollama获得回答
    # from ai_backend import chat_message
    # todo 导入同级的ai_backend.py中chat_message函数
    # 向ollama服务发送请求，获取指定的大模型回复信息
    # ollama帮我们运行大模型的，想和模型文件进行交互需要ollama
    assistant_content = chat_message(user_content)

    # 机器人回答问题
    st.chat_message('assistant').write(assistant_content)

    # todo 把机器人的回答添加到列表中
    st.session_state['messages'].append(
        {
            'role': 'assistant',  # 角色
            'message': assistant_content
        }
    )


# 终端启动命令：
# D:\ProgramData\anaconda3\python.exe -m streamlit run D:\BaiduNetdiskDownload\1.python基础\code\day08\04_聊天机器人.py


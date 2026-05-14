import streamlit as st

#设置窗口的标题
st.title("nb机器人")
st.divider()

#---------------初始化消息存储器start
#说明在session_state 中不存在消息存储器
if 'messages' not in st.session_state:
    #创建消息存储器，将message对应的value初始化为一个空的列表
    st.session_state['messages']=[]

    #将机器人发出的初始话语放入到消息中第一条
    #将信息保存到列表中
    st.session_state['messages'].append({
        'role':'assistant',
        'message':'你好，我是牛逼机器人，有啥能干的？'
    })
    print(st.session_state['messages'])

#---------------遍历打印消息存储器，将每一条消息都输出到页面中
for message_dict in st.session_state['messages']:
    #输出到页面
    st.chat_message(message_dict['role']).write(message_dict['message'])

    #用户消息输入框
user_content = st.chat_input('请输入您的问题')

if user_content:
    #如果用户输入了内容，需要将内容填充到机器人聊天窗口中
    st.chat_message('user').write(user_content)
    #将用户输入的内容保存到消息存储器中
    st.session_state['messages'].append({
        'role':'user',
        'message':user_content
    })
    #接下来；机器人进行智能回答，需要调用ollama，暂时模拟回答
    assistant_content='默认回答'
    #将机器人的回复内容，填充到聊天窗口中
    st.chat_message('assistant').write(assistant_content)
    #将机器人响应的消息数据，保存到消息存储器中
    st.session_state['messages'].append({
        'role':'assistant',
        'message':assistant_content
    })
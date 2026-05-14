import streamlit as st
#2.设置标题页面
st.title("nb机器人")

#3.设置分隔符
st.divider()

#4.为了更好的体验先让ai说一句
st.chat_message("assistant").write("hello 摩托")

#5.用户提问输入框
prompt=st.chat_input("请输入您的问题：")

#todo 以后用户的提问时页面获取的prompt写入下方write（），本次险些固定的问题

st.chat_message("user").write(prompt)

#6.AI回答
#todo 以后ai的回答通过调用大模型获取的答案，放到下面write（），本次先写固定的答案
st.chat_message("assistant").write("扎西得嘞")
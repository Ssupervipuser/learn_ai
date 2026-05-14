# D:\ProgramData\anaconda3\python.exe -m pip install ollama -i https://pypi.tuna.tsinghua.edu.cn/simple
# D:\ProgramData\anaconda3\python.exe -m pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple

# import ollama
import streamlit as st
from datetime import date


# 设置页面标题
st.title('传智教育用户注册')

# 设置分割线
st.divider()

# 用户名输入框
username = st.text_input(
    label='请输入用户名：',
    max_chars=50,
    key='username'
)
print(username)

password = st.text_input(
    label='请输入密码：',
    max_chars=50,
    key='password'
)

age = st.number_input(
    label='年龄',
    min_value=0,
    max_value=200,
    step=1,
    key='age'
)

gender = st.selectbox(
    label='性别',
    options=[
        '请选择...',
        '男',
        '女'
    ],
    index=0,
    key='gender'
)

st.radio(
    label='是否已婚',
    options=['是', '否'],
    horizontal=True, # True表示横置、False表示纵置
    key='married'
)

birthdate = st.date_input(
    label='出生日期',
    min_value=date(1900, 1, 1),
    max_value=date.today(), # 当日日期
    key='birthdate'
)


# 身高输入框
height = st.slider(
    label='身高',
    min_value=40.0,
    max_value=300.0,
    value=175.0,
    step=0.1,
    key='height'
)

# 提交按钮
submit_button = st.button(label='注册')
if submit_button:
    st.success('注册成功')
    print(
        f"注册成功！以下是您的信息:\n用户名: {username}\n密码: {password}\n年龄: {age}\n性别: {gender}\n出生日期: {birthdate}\n身高: {height} cm")
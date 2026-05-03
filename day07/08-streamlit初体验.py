import streamlit as st

st.title('学生管理系统注册页面')

st.write('欢迎光临')

uname = st.text_input('请输入账号:')
pwd = st.text_input('请输入您的密码:',type='password')

st.image('1.jpg')
"## 2级标题"
"### 3级标题"
"#### 4级标题"
"##### 5级标题"
"###### 6级标题"

import pandas as pd

st.write('dict字典形式的可交互表格')
st.dataframe(data={
    'name': ['张三', '李四', '王五'],
    'age': [18, 20, 22],
    'gender': ['男', '女', '男']
})

st.write('pandas中dataframe形式的可交互表格')
df = pd.DataFrame(
    {
        'name': ['张三', '李四', '王五'],
        'age': [18, 20, 22],
        'gender': ['男', '女', '男']
    }
)
st.dataframe(df)


a = 10
b = 20

st.write(a * b)

name = st.text_input('请输入你的名字：')

if name:
  st.write(f'你好，{name}')


st.audio('http://music.163.com/song/media/outer/url?id=447925558.mp3', format='audio/mp3')

st.video('http://vjs.zencdn.net/v/oceans.mp4', format='video/mp4')

# 用户信息
with st.chat_message("user"):
    st.write("Hello 👋")

# 机器人信息
message = st.chat_message("assistant")
message.write("Hello human")
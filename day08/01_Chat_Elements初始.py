import streamlit as st


# 搭建左侧导航栏
with st.sidebar:
    api_key = st.text_input('请输入Tongyi账号的API KEY:', type= 'password')

#设置标题
st.title('通义聊天机器人')

#创建一个文本输入框,输入机器人的回复
with st.chat_message("assistant"):  #机器人
    st.write('您好,我是您的AI助手,有什麽可以帮助您吗?')

#创建一个文本框,输入要提问的问题
#question = st.text_input('请输入问题')
with st.chat_message("user"):     #user: 用户
    st.text_input('请输入您要提问的问题:')

#创建提问消息的文本框
st.chat_input('请录入您要提问的问题')


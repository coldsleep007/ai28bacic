# 聊天机器人_前端代码
import streamlit as st
from background import get_response_msg


# def ai_view():
#     # 1- 聊天机器人的标题
#     st.title("黑马AI🤖")
#
#     # 2- 接收用户输入的问题
#     prompt = st.chat_input("😇请输入您的问题：")
#
#     # 3- 与后端进行交互，提交用户问题，得到返回答案
#     if prompt:
#         response_msg = get_response_msg(prompt)
#         st.chat_message("user").markdown(prompt)
#
#         # 4- 前端页面展示问题和问题答案
#         st.chat_message("assistant").markdown(response_msg)
#
#
# if __name__ == '__main__':
#     ai_view()

def ai_view():
    # 标题
    st.title("黑马AI🤖")
    # 接收用户输入
    prompt = st.chat_input("亲输入提问的问题：😇")
    # 调用后端函数获取答案
    if prompt:
        response_msg = get_response_msg(prompt)
        st.chat_message("user").markdown(prompt)
        st.chat_message("assistant").markdown(response_msg)


if __name__ == '__main__':
    ai_view()

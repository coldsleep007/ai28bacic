import streamlit as st
if __name__ == '__main__':
    # 输入用户的问题
    prompt = st.chat_input('请输入问题')
    if prompt:
        st.write(f'你的问题是: {prompt}')

    # 展示用户的问题
    with st.chat_message("user"):
        st.write(prompt)

    # 展示ollama的回答
    msg = st.chat_message("assistant")
    msg.write('大模型的回答是XXX')





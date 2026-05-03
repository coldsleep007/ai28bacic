# 聊天机器人_后端代码
"""
    思路：
        前端用户输入问题 -> 后端代码处理 -> Ollama ->指定的大模型
"""
import ollama


def get_response_msg(prompt):
    # 将问题以HTTP请求的方式发送给Ollama
    response = ollama.chat(model="qwen2:0.5b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]


if __name__ == '__main__':
    prompt = "介绍下广州"
    response_msg = get_response_msg(prompt)
    print(response_msg)

import ollama


def get_message(prompt):
    response = ollama.chat(model="qwen2:0.5b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]


if __name__ == '__main__':
    while True:
        question = input("请输入问题：")
        if question == "break":
            break
        result = get_message(question)
        print(get_message(question))

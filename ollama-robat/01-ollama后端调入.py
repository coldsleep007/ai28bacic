import ollama

if __name__ == '__main__':
    question = '介绍一下广州'
    response = ollama.chat(model="qwen2:0.5b", messages=[{"role": "user", "content": question}])
    print(response, type(response))
    print(response["message"]["content"])
    pass

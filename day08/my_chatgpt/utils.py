#这里写的是核心业务逻辑

# 1. 导包
from langchain_community.llms import Tongyi    #通义模型
from langchain.chains import ConversationChain  #llm模型+记忆体
from langchain.prompts import ChatPromptTemplate #聊天模版
from langchain.memory import ConversationBufferMemory #会话记忆体

# 2. 定义一个函数, 用于发起请求, 返回结果.
def get_response(prompt, memory, api_key):
    # 3. 创建模型对象
    llm = Tongyi(model='qwen-max', dashscope_api_key=api_key)
    # 4. 创建chains链
    chains = ConversationChain(llm=llm, memory=memory)
    # 5. 发起请求, 获取结果.
    response = chains.invoke({'input': prompt})
    # 6. response是记忆体, 很对之前会话, 本次会话包含在一个response的key中
    return response['response'] # 这样写是只取本次会话的response


# 在main函数中测试
if __name__ == '__main__':
    # 1. 组装模板
    prompt = '世界上第二高的山峰是哪一座?'

    # 2. 创建记忆体对象
    memory = ConversationBufferMemory(return_messages=True)

    # 3. 获取API_KEY
    api_key = 'sk-68130f72b3144e2f886ab07660a212b4'

    # 4. 调用函数, 获取结果.
    result = get_response(prompt=prompt, memory=memory, api_key=api_key)
    # 5. 打印结果
    print(result)

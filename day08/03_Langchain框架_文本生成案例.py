#导包
from langchain_community.llms import Tongyi

#创建LLM模型
llm = Tongyi(model = 'qwen-max')

#用死循环改成循环版
while True:
    # 提示用户录入信息
    prompt = input('亲输入你要问的问题:')

    # 向llm模型发起请求,获取相应处理结果
    result = llm.invoke(prompt)

    # 打印结果
    print(f'结果是:{result}')

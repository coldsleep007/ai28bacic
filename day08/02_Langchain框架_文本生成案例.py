#需求:基于Langchain调用tongyi,实现文本生成(文本扩写)

#导包
from langchain_community.llms import Tongyi

#创建提示词
prompt = "从前有座山，山里有座庙"

#创建LLM模型,并调用接口

llm = Tongyi(
    model = 'qwen-max',
    dashscope_api_key = 'sk-10bd441227ae4c15a3675b5af337135a'
)
#llm = Tongyi(model = 'qwen-max')

#调用接口 生成文本
result = llm.invoke(prompt)

# 5. 返回最终结果
print(f"提示词：{prompt}")
print(f"最终结果：{result}")
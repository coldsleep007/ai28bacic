# 1. 导入相关包.
from langchain_community.llms import Tongyi

# 2. 初始化模型.
llm = Tongyi(
    model = 'qwen-max'
)

# 3.定义提示词.
prompt = """
请为一下功能生成一段Python代码: 求两个数的最大公约数
"""

# 4. 调用模型生成代码.
result = llm.invoke(prompt)

# 5. 打印结果.
print(result)
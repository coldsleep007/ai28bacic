#需求：基于LangChain中的ChatPromptTemplate构建一个翻译器，英语翻译汉语
#Prompt：I'm so hungry I could eat a horse

#导包
from langchain_community.llms import Tongyi       #通义模版
from langchain.prompts import ChatPromptTemplate   #聊天模版

llm = Tongyi(model = 'qwen-max')

#创建消息模版类格式
prompt_template = ChatPromptTemplate.from_messages([
    ('system', '你一个语言翻译工具, 你可以把{input_language}翻译为{output_language}'),
    ('human', '用户文本: {text}\n, 翻译后的语言风格{style}')
])

# 4. 根据以上模型, 传入模板消息变量值, 组成最终的消息体.
# 定义1个变量, 代表用户要翻译的文本.
text = input('请输入您要翻译的内容: ')
prompt_value = prompt_template.invoke({
    'input_language': '英语',
    'output_language': '中文',
    'text': text,
    'style': '文言文'
})

# 5. 调用模型, 得到结果.
result = llm.invoke(prompt_value)
print(result)
f = open('F:/pythonproject/ai28bacic/day06/data/a.txt','r',encoding='UTF-8')

print(f.read())

"""
往文件中写信息:
    write(数据)       往文件中写数据.
    writelines()     一次写多行.

细节:
    1. 注意写数据的模式,  w: write,覆盖写入.  a: append,追加写入.
    2. 读的时候, 如果 数据源文件不存在, 会报错.  No Such File Or Directory...
    3. 写的时候, 如果 目的地文件不存在, 会自动创建.

f = open('./data/b.txt','a',encoding = 'UTF-8')
f.write('hello world\n')
f.write('好好学习,天天向上')

f.close()
"""
src_f = open('./data/a.txt','r',encoding = 'utf-8')
dest_f = open('./data/b.txt','w',encoding = 'utf_8')
#data = src_f.read()
#dest_f.write(data)

# 方式3: 循环读取, 读一行, 写一行.  或者 一次性读写指定的字节数, 一般是: 1024的整数倍.
while True:
    # 一次性读取 8192个字节, 8 * 1024 = 8192个字节 = 8KB
    data = src_f.read(8192)
    # 核心细节: 如果读不到数据了, 即读取到文件末尾了, 结束读取.
    # if len(data) == 0:        # 可以判断长度
    if data == '':              # 也可以判断是否为空
        break
    # 把读取到的数据, 写到目的地文件.
    dest_f.write(data)

# 3. 关闭文件.
src_f.close()
dest_f.close()

#项目工程路径下有一个python.txt的文件，请读取其中内容，并打印文件中的每一行数
f = open('./data/python.txt','r',encoding='utf-8')
while True:
    data = f.readline()
    if len(data) ==0:
        break
    print(data)
f.close()

name = input("请输入姓名：")
age = input("请输入年龄：")
gender = input("请输入性别：")

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(f"姓名：{name}\n年龄：{age}\n性别：{gender}")

print("写入完成！")
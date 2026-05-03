"""
文件 介绍:
    概述:
        无论是 windows, Linux, Mac系统, 都是采用 文件 来管理数据的, 它们都是 文件管理系统.
        之所以用文件来管理数据, 原因是因为: 内存中的数据是临时存储的, 电脑管理了, 数据就丢失了.
        文件: 可以实现 永久 存储数据.
    文件的类型:
        文本文档, 图片类型, 视频类型, 音频类型......
    文件的操作步骤:
        1. 打开文件.
        2. 读写操作.
        3. 关闭文件.

    打开文件 涉及到的API(Application Programming Interface, 应用程序编程接口), 就是: 别人写的 函数.
        文件对象名 = open('文件路径', '打开模式', 码表)        # 参3为可选项, 针对于 中文有效.
    读取文件信息:
        read(num)       一次读取num个字节的数据, 不写就一次性读取所有的数据.
        readline()      一次读取一行.
        readlines()     一次性读取读完所有行, 且会把每行数据封装到 1个列表中.
    关闭文件:
        文件对象名.close()

细节:
    1. Python中, 路径的写法, 要么用 /,  要么用 /, 要么用 r'一个\就行', 即: r'\' 会取消 \的转移含义, 当做1个普通字符来用.
    2. 相对路径默认是相对于 当前项目的路径来写的, 即: 你直接写 1.txt, 想到于是  /当前项目路径/1.txt
"""
#
# f = open(file="F:/pythonproject/ai28bacic/day06/data/a.txt", mode='w', encoding='utf-8')
# f.write('来黑马,月薪过两万')
# f.close()
# f = open(file="./data/a.txt", mode='a', encoding='utf-8')
# f.write('\n来黑马,月薪过两万')
# f.close()
# with open('./data/a.txt', 'w', encoding='utf8') as f:
#     for i in range(10):
#         f.write('黑马程序员\n')
# f = open(file="./data/a.txt", mode='r', encoding='utf-8')
# result = f.read(2)   # 读取指定长度内容 内部有指针,根据上次读取的地方继续读取
# print(result)
# result = f.read()   # 读取所有内容
# print(result)
# print(f.readline())  # 返回字符串
# print(f.readlines())  # 读取多行,以列表的方式返回 每行的回车换行符也会被读取
# f.close()
# g = open('./a.txt','r')

# print(f'文件对象名:{f}')
# print(f.read())

f = open('./data/a.txt', 'r', encoding='utf-8')
while True:
    result = f.readline()
    print(result, end='')
    if result == '':
        break
f.close()

f = open('./data/a.txt', 'r', encoding='utf-8')
while True:
    result = f.read()
    print(result, end='')
    if result == '':
        break
f.close()
f = open('./data/a.txt', 'r', encoding='UTF8')
result = f.read(1)
print(result, end='')
result = f.read(1)
print(result, end='')
f.close()

















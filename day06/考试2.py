"""
定义一个字符串，如
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。 [上传文件题]
"""
from random import randint
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
str2 = ''
for i in range(4):
    index = randint(0, len(str1) - 1)
    str2 += str1[index]
print(str2)
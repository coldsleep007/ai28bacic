"""
定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，
求列表里的数字元素和字典里的value值它们的累积结果
例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},
定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6）
"""
import random


def fun(a, b):
    count = 0
    for i in a:
        count += i
    for value in b.values():
        count += value
    print(count)


list1 = [1, 2, 3]
dict1 = {'a': 4, 'b': 5, 'c': 6}
fun(list1, dict1)
fun([1, 2, 3], {'a': 4, 'b': 5, 'c': 6})

"""
定义一个字符串，如str1 = "0123456789abcdABCD"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码"""

# def fun2(s):
#     t = ''
#     for i in range(4):
#         a = random.randint(0, len(s))
#         t +=  s[a]
#     print(t)
# 
# 
# 
# fun2("0123456789abcdABCD")


#
# def fun(lst, dct):
#     total = 0
#
#     for item in lst:
#         if isinstance(item, (int, float)):
#             total += item
#     for value in dct.values():
#         if isinstance(value, (int, float)):
#             total += value
#     return total
#
#
#
# result = fun([1, 2, 3], {'a': 4, 'b': 5, 'c': 6})
# print("累积结果为：", result)
#


fn1 = lambda: 100
fn2 = lambda a, b: a + b
fn3 = lambda a, b: a if a > b else b
print(fn1())
print(fn2(1, 2))
print(fn1)
print(id(fn1))
result = 1 if 1 > 2 else 2
#
print(result)

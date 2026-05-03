"""
字典遍历介绍:
    概述:
        所谓的遍历, 就是逐个获取容器中 每个元素的操作.
    字典遍历方式:
        思路1: 根据 键 获取其对应的值.              理解为: 根据 丈夫 找 妻子.
        思路2: 根据 键值对 获取其对应的 键 和 值.    理解为: 根据 结婚证 找 丈夫 和 妻子.
"""
# 1. 定义字典, 记录: 键值对元素.
dict1 = {'乔峰': '阿朱', '虚竹': '梦姑', '杨过': '小龙女', '郭靖': '黄蓉'}
keys = dict1.keys()
for key in dict1.keys():
    value = dict1.get(key)
    print(value)

for key in dict1.keys():
    value = dict1.get(key)
    print(f'{key}<=>{value}')

for key in dict1.keys():
    print(f'{key}<=>{dict1.get(key)}')
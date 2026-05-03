"""
组包和拆包解释:
    概述:
        组包 和 拆包 是Python中的一种独有写法.
    格式:
        把 多个值 => 1个变量 的过程, 称之为: 组包.
        把 1个(容器)变量 => 多个变量值 的过程, 称之为: 拆包.
    应用场景:
        1. 一次性获取到 元组, 列表, 字典中的每个数据.
        2. 交换变量.
"""

# 组包.   多 => 1
list1 = [11, 22, 33, 44, 55]
tuple1 = ('aa', 'bb', 'cc')
dict1 = {'name': '张三', 'age': 23}

# 拆包.
# 从 列表 拆包
a, b, c, d, e = list1
print(a, b, c, d, e)

# 从 元组 拆包
x, y, z = tuple1
print(x, y, z)

# 从 字典 拆包, 只能获取 键 的值.
k1, k2 = dict1
print(k1, k2)

a = 1
b = 2
a, b = b, a
print(a, b)


def my_fn():
    return 1, 2, 3


result = my_fn()
print(result, type(result))

result_2 = 1, 2, 3
print(result_2, type(result_2))

# 拆包：将元组中的元素，一个个拆解出来给到变量
# 注意：等号左边的变量个数要与元组中的元素个数，完全一致
num1, num2 = (1, 2)
print(num1, num2, type(num1), type(num2))

a, b = (1, 2)
print(a if a > b else b)


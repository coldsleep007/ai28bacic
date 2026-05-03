"""
容器类型的公共操作-函数:
    len()                       获取长度
    del 或者 del()               删除
    max()                       获取最大值
    min()                       获取最小值
    range(start, end, step)     生成指定范围内的数据
    enumerate()                 基于可迭代类型(字符串, 列表, 元组等), 生成 下标 + 元素的方式, 即: ['a', 'b', 'c']  => [(0, 'a'), (1, 'b'), (2, 'c')]
"""
list1 = [10,50,20,30,66,22]

print(len(list1))

#del list1
del(list1[1])
print(f'list1:{list1}')
print(max(list1))
print(f'range:{list(range(1,5,2))}')

print(enumerate(list1))

for i in enumerate(list1):
    print(i)

for i in enumerate(list1,5):
    print(i)
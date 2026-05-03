s = 'abcdefgh'
print(s[::-1])
print(s[1:3])

# 1. 定义字符串变量s1, 记录要操作的数据.
s1 = 'hello and python and sql and linux'

# 2. 演示 replace()函数.
s2 = s1.replace('and', 'or')  # 不写个数, 替换所有
s3 = s1.replace('and', 'or', 2)  # 写了个数, 写几个替换几个.

# 3. 打印结果:
print(f's1: {s1}')  # s1是不可变类型, 内容不变.
print(f's2: {s2}')
print(f's3: {s3}')
print('-' * 28)

# 4. 演示 split()函数.
list1 = s1.split('and')
print(type(list1))  # <class 'list'> 列表, 也是容器类型的一种.
print(list1)  # ['hello ', ' python ', ' sql ', ' linux']
list1 = s1.split('and', 2)
print(type(list1))  # <class 'list'> 列表, 也是容器类型的一种.
print(list1)  # ['hello ', ' python ', ' sql ', ' linux']

s = 'hello'
s1 = ','.join(s)
s2 = s1.split(',')
print(s2)

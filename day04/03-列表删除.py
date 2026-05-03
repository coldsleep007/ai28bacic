s = [10,20,30,25]
s.reverse()
print(s)
s.sort()
s.sort(reverse=True)
print(f's:{s}')

name_list = [['刘怡铭', '陈正', '蔡徐坤'], ['王心凌', '王祖贤', '张曼玉'], ['李白', '杜甫', '李贺']]


# 2. 获取指定的元素.
print(name_list[1])         # ['王心凌', '王祖贤', '张曼玉']
print(name_list[1][0])      # '王心凌'
print(name_list[2][1])      # '杜甫'
print('-' * 28)
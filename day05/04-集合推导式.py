set1 = {i for i in range(10)if i %2==0}
print(set1)

dict1 = {i:i**2 for i in range(1,6)}
print(dict1)

# 需求4: 把下述的两个列表, 拼接成1个字典.
# 细节: 两个列表的元素个数(长度) 要 一致.
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'male']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)
"""
list1 = [1,2,3,4]

for value in list1:
    print(value)

for i in range(len(list1)):
    print(list1[i])

print(list1[-1])

list2 = [10,20,30,40,50]
list3 = ['a','b','c']
#list2.extend(list3)
list2.append(list3)
list2.insert(-2,100)
#list2.index()
print(f'list2:{list2}')
print(f'list3:{list3}')

my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
list1 = []
for i in my_list:
    if i[-1]=='s':
        list1.append(i)
print(my_list)
print(list1)

my_list = ["spring", "look", "strange" "curious", "black", "hope"]
for i in my_list:
    if i[0] =='s':
        my_list.remove(i)
print(my_list)

my_list[1]=my_list[-1]
my_list.insert(1,'sorry')
print(my_list)

list1 = [11, 4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]

list3 = list1+list2
list4=[]
for i in list3:
    if i not in list4:
        list4.append(i)
print(list4)

list1 = [11, 4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]

list3 = list1+list2
list4=set(list3)
list5 = list(list4)
list5.sort(reverse=False)
print(list5)

list1 = ['bds', 2]  # 不同数据类型可以存放在一个列表中
print(list1, type(list1))
list2 = list1
print(list2, type(list2))
print(list1.index(2))
print(type(list1[1]))
print(list1.count('bds'))
print(2 in list1)

list1.append('hello')
print(list1)
list1.extend(list2)
print(list1)

list1.insert(1, 'world')
list1.insert(10, 'world')
print(list1)
print(list1[::-1])
del list2[0]
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del list1[0]
print(list1)
b = list1.pop(0)
print(b)
list1.remove(4)
print(list1)
print(list1.reverse())
print(list1)
print(list1.sort(reverse=False))
print(list1)

list2 = [11,12,13]
print(list1+list2)

for i in list1:
    print(i,end='\t')
list2.extend([7])
print(list2)





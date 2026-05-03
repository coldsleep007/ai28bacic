list1 = []
for i in range(10):
    list1.append(i)
print(list1)

list2 = [i for i in range(10) if i % 2 == 0]
print(list2)

list3 = list(range(10))
print(list3)

s1 = set(i for i in range(10))
print(s1)

dict1 = {i: i ** 2 for i in range(10)}
print(dict1)

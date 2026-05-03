tuple3 = (1, 2, 3, 4, 5)
print(tuple3)
print(tuple3[:3])

tuple1 = ('a', 5, 'hello', 0.36)
for i in tuple1:
    print(i)
list1 = [1, 2, 3]
tuple2 = (list1, 'string', '你好')
for i in tuple2:
    print(i)

print(tuple3[0::2])
print(tuple3.index(1))
print(tuple3.count(1))
print(len(tuple3))
tuple(list1)  # 不行
print(list1, type(list1))







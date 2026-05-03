s1 = {6, 7, 8, 2, 4, 3, 9, 'String', 13.006}
print(s1, type(s1))
s2 = {}
print(s2, type(s2))
s3 = set()
print(s3, type(s3))
tuple1 = (1, 1, 5, 7, 9, 6, 3, 4, 4, 5)
print(tuple1)
tuple1 = tuple(set(tuple1))
print(tuple1)
s1.clear()
print(s1, type(s1))
s4 = {1, 2, 7, 8}
s5 = {1, 3, 7, 6}
print(s4.intersection(s5))
print(s4)
print(s5)

import math_test

def fun(a, b):
    count = 0
    count = sum(a)
    count += sum(b.values())
    print(count)



list1 = [1, 2, 3]
dict1 = {'a': 4, 'b': 5, 'c': 6}
fun(list1, dict1)
fun([1, 2, 3], {'a': 4, 'b': 5, 'c': 6})
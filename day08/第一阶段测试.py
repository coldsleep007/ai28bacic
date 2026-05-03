import numbers

"""
def fun(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    for value in kwargs.values():
        total += value
    return total


my_list = [1, 2, 3]
my_dict = {'a': 4, 'b': 5, 'c': 6}
result = fun(*my_list, **my_dict)
print(result)


count = 3
while count > 0:
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username == 'admin' and password == 'admin888':
        print("登录成功")
        break
    else:
        count -= 1
        if count > 0:
            print(f"用户名或密码输入错误，你还有{count}次机会")
        else:
            print("用户名或密码输入错误，已无重试机会")

li = [1,2,3]
def Modify(li):
    li.append(4)
    print(li)
print(li)
Modify(li)
fn = Modify
print(fn)
fn(li)
print(li)
print(fn(li))
"""
f = open("1.txt",'w')
f.write("welcome to python!")
f.close()

f = open("1.txt",'w')
f.write("python is best language!")
f.close()
f = open("1.txt",'r')
print(f.read())
f.close()

f = open("1.txt",'w')
f.close()
f = open("1.txt",'r')
print(f.read())
f.close()

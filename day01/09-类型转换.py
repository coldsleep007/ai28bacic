print(eval('10.3'))
print(eval('22'))
print(eval('True'))

name = '夯哥'
print(eval('name'))  # 相当于去掉 ' name '的引号, name就不是字符串了, 而是 变量名.

print(type(eval('10.3')))
print(type(eval('22')))
print(type(eval('True')))

print(type(eval('10.3')))
print(type(eval('22')))
print(type(eval('True')))

c1 = '可乐'
c2 = '牛奶'
c = ' '

c = c1
c1 = c2
c2 = c
print(c1)
print(c2)

a = 1
print("a=%d" % a)

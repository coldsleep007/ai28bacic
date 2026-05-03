# password = input('请输入密码:')
# print(f'您输入的密码是:{password}')

# a = input('第一个数字:')
# b = input('第二个数字:')
# print(f'a+b是:{int(a)+int(b)}')
# print(type(a))

# print('string', end='\r\n')

# int->float
a = float(10)
print(a, type(a))

# int->string
a = str(10)
print(a, type(a))

# float->int 只保留整数部分,小数部分彻底删除
a = int(10.983)
print(a, type(a))

# bool->int
a = int(False)
print(a, type(a))

# int->bool
a = bool(96)
print(a, type(a))

# float->bool
a = bool(0.0)
print(a, type(a))

# string->bool
a = bool('string')
print(a, type(a))
a = bool('')
print(a, type(a))
a = bool(' ')
print(a, type(a))
a = bool('False')
print(a, type(a))

# eval() 根据传递的内容动态决定类型
a = eval('10')
print(a, type(a))
a = eval('True')
print(a, type(a))
a = eval('1.99')
print(a, type(a))
# a = eval('hello')  # 错误
# print(a, type(a))
print(type(eval("\'abc\'")))




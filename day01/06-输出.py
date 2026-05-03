name = '威震天'
age = 99
salary = 1000.1235
flag = True  # 标记是否是反派, True: 是, False: 不是

# 演示 1. 输出单个值.
print('我的\n姓名是: ' + name)
print('我的姓名:' + name)
# print('我的年龄是: ' + age)      # 报错, Python中 字符串 和 整数不能进行 加法运算(拼接操作)
print('-' * 28)
print(age)

# 上述的代码, 完整写法如下.
print('hello', end='\n')  # end='\n', 是程序默认给 print()函数添加的, 即: 换行输出.
print('world', end='\n')

print('hello', end='\t')  # 空格
print('world', end='\n')
print('I\'m Tom')

age = 100
print("我今年%d岁了"% age)
print(f'我叫{name},今年{age:05d}岁了,工资是{salary:.3f}')
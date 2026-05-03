# a,b,c = 7,2,18
# max = a if a>b else b if a >c else c if c>b else b
# print(f'最大数{max}')
# i = 1
# sum1 = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum1 = sum1 + i
#     i += 1
# print(f'1-100偶数相加一共是:{sum1}')
i = 3
name = 'root'
password = '123456'

while i > 0:
    name1 = input('亲输入用户名:')
    password1 = input('亲输入密码:')

    if (name == name1) and (password == password1):
        print('登陆成功!')
        break
    else:
        i = i-1
        print(f'您还有{i}次机会')

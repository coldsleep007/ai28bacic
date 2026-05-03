"""
接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，
则提示用户登录成功，其他情况则提示用户名或密码输入错误，只有3次输入机会。
"""
name = 'admin'
pwd = 'admin888'
for i in range(3):
    name1 = input("请输入用户名：")
    if name1 == name:
        pwd1 = input("请输入密码：")
        if pwd1 == pwd:
            print("登录成功")
            break
        else:
            print("密码输入错误")
    else:
        print("用户名输入错误")









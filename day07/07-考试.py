

"""
s1 = input('亲输入姓名:')
s2 = input('亲输入年龄:')
s3 = input('亲输入性别:')
try:
    f = open('output.txt', 'w', encoding='utf-8')

except Exception as e:
    print(e)

else:
    f.write(s1)
    f.write(s2)
    f.write(s3)

finally:
    print('写入完成!')
"""

"""
count = 0
with open('numbers.txt','r',encoding='utf-8') as a:

    while True:
        data = a.readline()
        if len(data)==0:
            break
        count = count + int(data)
    print(count)


try:
    f1 = open('python.txt', 'r', encoding='utf-8')

except Exception as e:
    f2 = open('python.txt', 'w', encoding='utf-8')
    s = '开启文件失败，执行except中的代码'
    f2.write(s)
    print(e)


else:
    while True:
        data = f1.readline()
        if len(data) == 0:
            break
   f2.close()

try:
    with open('python.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    with open('python.txt', 'w', encoding='utf-8') as file:
        file.write("开启文件失败，执行except中的代码")

try:
    num = input("请输入一个整数：")
    num = int(num)
except ValueError:
    print("输入无效，请输入一个有效的整数！")
else:
    square = num ** 2
    print(f"{num} 的平方是 {square}")
"""
try:
   print(number)
except NameError as errorMsg:
   print('产生错误了:%s' % errorMsg)
else:
   print('没有捕获到异常，真高兴')
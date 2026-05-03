# year = input('亲输入你的年龄')
# 把年龄转成int型
# year = eval(input('亲输入你的年龄'))
# year2 = int(input('亲输入你的年龄'))
# if year > 18:
#     print('您已成年')
# print('您未成年')
import random
i = 1
total = 0
while i <= 100:
    # print(i)
    if i % 2 == 0:
        total += i
    i = i + 1
print(total)

num = random.randint(1, 2)
print(num)

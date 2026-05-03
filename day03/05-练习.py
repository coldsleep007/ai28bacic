import random

s = 'hello'
print(s[0::2])

b = "dfjknvk.png"
if b.rfind('.png')>-1:
    print('是')
"""
password = 123456
name = "python"
while True:
    password1 = int(input('亲输入密码:'))
    name1 = input('亲输入用户名:')
    if(password1==password)and(name1==name):
        break;
    print("cuowu")

num = random.randint(0,101)
while True:
    num1 = int(input('亲输入数字:'))
    if num ==num1:
        print(f'恭喜你猜对了,{num}')
        break;
    elif num>num1:
        print('猜小了')
    elif num <num1:
        print('猜大了')

i=2
j=2
flag=0
while i <=100:
    while j<i:
        if i % j==0:
            flag=1
            break
        else:
            j=j+1
    if flag==0:
        print(i)
    flag=0

    j=2
    i=i+1


word  = '鲁迅说:"我没有说过这句话"'
print(word)

word='abcdefghi'
print(word[2:7:2])
print(word.find('cd'))
print(word.index('cd'))
"""

words = " great craTes Create great craters, But great craters Create great craters "

# 判断单词great是否在这个字符串中
if 'great' in words:
	# 将每一个great替换成greats
    words = words.replace("great", "greats")

    # 将单词变成小写
    words = words.lower()

    # 将每一个单词的首字母都大写
    words = words.title()

    # 去除首尾的空白
    words = words.strip()

    # 最后进行输出
    print(words)

else:
    print("great不在该字符串中")
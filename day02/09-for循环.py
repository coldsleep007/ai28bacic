# 需求1: for循环 遍历字符串.
s = 'heima'
for i in s:
    # i 就是 字符串s中的每个字符, 例如: 'h', 'e', 'i', 'm', 'a'
    print(i)
print('-' * 28)

# 需求2: for循环 遍历字符串, 判断是否有指定字符, 如果有, 就打印: 黑马AI28期
for i in s:
    # i 就是字符串s中的每个字符, 例如: 'h', 'e', 'i'...
    print(i)

    # 判断当前字符串是否是 'i', 如果是, 就输出 黑马AI28期
    if i == 'i':
        # 走这里, 说明存在字符i
        print('黑马AI28期')
print('-' * 28)

for i in range(1,6):
    print(i)
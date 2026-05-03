i = 1
while i < 1000:
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if (a * a * a + b * b * b + c * c * c) == i:
        print(f'{i}是水仙花数\n')
    i += 1
# //整除

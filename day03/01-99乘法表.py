for i in range(1, 10):  # 外循环控制 行数, 例如: i = 3
    for j in range(1, i + 1):  # 内循环控制 列数, 此时: j = 1, 2, 3
        print(f'{j} * {i} = {i * j}', end='\t')
    # 走到这里, 说明一行打印完毕, 记得换行.
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()

import keyword

# print(keyword.kwlist)

# i = 1
# for i in range(1, 10):
#     j = 1
#     for j in range(1, i+1):
#         if j == i:
#             print(f'{j}*{i}={j*i}', end='\n')
#         else:
#             print(f'{j}*{i}={j*i}', end='\t')
#         j += 1
#     i += 1


# i = 9
# for i in range(9, 0, -1):
#     j = 1
#     for j in range(1, i+1):
#         if j == i:
#             print(f'{j}*{i}={j*i}', end='\n')
#         else:
#             print(f'{j}*{i}={j*i}', end='\t')
#         j += 1
#     i -= 1


m = input('请输入1到9数字:')
i = 9
for i in range(int(m), 0, -1):
    j = 1
    for j in range(1, i+1):
        if j == i:
            print(f'{j}*{i}={j*i}', end='\n')
        else:
            print(f'{j}*{i}={j*i}', end='\t')
        j += 1
    i -= 1

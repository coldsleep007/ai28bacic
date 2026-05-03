print('----- start -----')
print('hello 1' + 'aa' + '5' + '10')
print('hello2')
print('hello3')
print('----- end -----')
flag = 0
i = 1
for i in range(1, 101):
    j = 2
    for j in range(2, i):
        if i == 1 or i == 2:
            break
        else:
            if i % j == 0:
                flag = 1
                break
        j += 1
    if flag == 0:
        print(i)
    flag = 0
    i += 1

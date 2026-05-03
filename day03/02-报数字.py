n = int(input('亲输入学生人数:'))
count=0
for i in range(1,n+1):
    if (i%10==7)or(i%7==0):
        continue
    count+=1
print(count)
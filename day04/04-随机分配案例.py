import random

class1 = [[],[],[]]
num = [1,2,3,4,5,6,7,8,9]
for i in range(len(num)):
    class_id = random.randint(0,2)
    class1[class_id].append(i)
for i in range(len(class1)):
    for j in range(len(class1[i])):
        print(class1[i][j])
print(class1)


count = 0
with open('./data/numbers.txt','r',encoding = 'utf-8')as f:
    while True:
        data = f.readline()
        if len(data) ==0:
            break
        count+=int(data)
    print(count)

word_count = {}
with open('./data/input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

with open('output.txt', 'w', encoding='utf-8') as outfile:
    for word, count in word_count.items():
        outfile.write(f"{word}: {count}\n")


# 初始化总和为0
total = 0

# 逐行读取文本文件中的数字并累加求和
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

# 输出求和结果
print("求和结果：", total)

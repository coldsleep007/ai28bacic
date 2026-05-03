s1 = '我爱'
s2 = 'Python!' * 3
s = "2022china"
print(s[-1] + s[2] * 2)

lst1 = ['北京', '上海', '广州']
lst1.append('深圳')
print(lst1)
"""
prices = [10,25,15,70,36,45,50]
prices.sort(reverse = False)
print(prices)
max1 = max(prices)
print(max1)
min1 = min(prices)
print(min1)

count = 0
for i in prices:
    count+=i
average = count/len(prices)
print(average)

my_list = [1,2,3,4,5]
count = 0
for i in my_list:
    count=count+i
print(count)

my_list1 = my_list
my_list=my_list+my_list1
print(my_list)

print(my_list.index(3))
print(max(my_list))
print(min(my_list))
"""
i = 1
while i < 11:
    if i % 2 == 0:
        i = i + 1
        continue
    else:
        print(i)
        i = i + 1
count = 0
for i in range(1, 101):
    if (i % 7 == 0) and (i % 5 != 0):
        count = count + i
        print(i)
print(count)
cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]

cart_items = [item[0] for item in cart]
expensive_items = [item[0] for item in cart if item[1] >= 3]
cart_doubled = [(item[0], item[1] * 2) for item in cart]

print("cart_items:", cart_items)
print("expensive_items:", expensive_items)
print("cart_doubled:", cart_doubled)

s = "hello world"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"{char}:{count}")

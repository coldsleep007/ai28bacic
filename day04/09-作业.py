# list1 = [11, 22, 33, 22, 11, 55]
# list1 = list(set(list1))
# print(list1)

# str1 = input('亲录入字符串:')
# dict1 = {}
# for i in str1:
#     dict1[i] = dict1.get(i, 0)+1
# for i in dict1:
#     print(f'{i}({dict1[i]})', end='')

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# count = 0
# for i in set1:
#     if i % 2 !=0:
#         count +=i
# print(count)
#
# list1 = [2, 5, 3, 7, 5, 7]
# max = list1[1]
# min = list1[0]
# count = 0
# for i in list1:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# for i in range(min, max):
#     if i not in list1:
#         count += i
# print(count)

# 容器间只要满足语法要求，可以任意嵌套
# 需求：存储学生信息
stus_info = {
    "1001": {
        "name": "赵云",
        "age": 18,
        "score": [90, 87, 67, 87, 99],
        "addr": ("北京", "广州", "深圳")
    },
    "1002": {
        "name": "项羽",
        "age": 22,
        "score": [34, 64, 9, 10],
        "addr": ("北京", "广州", "深圳")
    }
}
print(stus_info["1002"]["score"][2])
stus_info["1002"]["score"][2] = 120
print(stus_info, type(stus_info))
print(stus_info.get("1002").get("score"))
# 将项羽考试成绩9分改成99分
stus_info.get("1002").get("score")[2] = 99
print(stus_info)
print(stus_info.__getitem__("1002"))
s1, s2, s3, s4 = stus_info.__getitem__("1001")
print(s1)
print(s2)
print(s3)
print(s4)
s1, s2 = stus_info.items()  # 用元组方式返回两对键值对
print(s1)
print(s2)

"""
dict1 = {'杨过':'小龙女', '郭靖':'黄蓉', '张无忌':'赵敏'}
dict2 = {}
dict3 = dict()
print(f'dict1:{dict1}')
print(f'dict1:{dict2}')
print(f'dict1:{dict3}')
dict1['妹妹'] = '小妹'

print(f'dict1:{dict1}')
#$dict1.clear()
#del dict1

dict1['杨过'] = '妹妹'
print(f'dict1:{dict1}')
print(dict1.get('杨过'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())   #列表嵌套元祖

# 1. 定义一个空字典 my_dict
# 2. 定义一个字典 my_dict1,字典存在以下键值对,name:isaac, age:18, pi:3.14,
# 3. 打印my_dict1和my_dict1 的类型
# 4. 输出 my_dict1中18 这个数据
# 5. 求my_dict1中元素的个数
# 6. 思考:通过字典的 key 访问和 get 方法访问,两者之间有什么不同
# 7. 修改字典my_dict1中age 的值为 19并输出
# 8. my_dict1中添加一个元素, gender: 男, 并输出打印
# 9. 删除my_dict1中 key 为 pi 的键值对(元素)
# 10. 清空字典my_dict1中的内容
# 11. 删除字典变量my_dict1
# 12. 现在是否还能使用 my_dict1 变量
my_dict = dict()
my_dict1 = {"name":"isaac", "age":"18", "pi":"3.14"}
print(my_dict1,type(my_dict1))
my_dict1['age'] = 19
print(my_dict1,type(my_dict1))
print(my_dict1['age'])
age = my_dict1.get('age')
print(age)
leng = len(my_dict1)
print(leng)
del my_dict1['pi']
my_dict1.clear()
print(my_dict1,type(my_dict1))
del my_dict1

dict1 = {'name':'chuanzhi','age':18}
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for key,value in dict1.items():
    print(key,value)
    """
# 编写一个程序将字符串转换为字典例如:输入:
# '5=Five 6=Six 7=Seven'
# 输出: {'5': 'Five', '6': 'Six', '7': 'Seven'}

str1 = '5=Five 6=Six 7=Seven'
dict1 = {}
list1 = str1.split(' ')
print(str1.split(' '))

for i in list1:
    key, value = i.split('=')
    print(i[2])
    dict1[key] = value
print(dict1)

def my_func(a, b, fn):
    """
    自定义函数, 根据传入的规则, 来计算两个整数的结果.
    :param a: 要操作的第1个数据
    :param b: 要操作的第2个整数
    :param fn: 具体的 计算规则 函数.
    :return: 具体的计算结果.
    """
    return fn(a, b)

print(my_func(10,20,lambda a,b:a if a>b else b))
print(my_func(10,20,lambda a,b: a+b))
print(my_func(10,20,lambda a,b: a-b))
print(my_func(10,20,lambda a,b: a*b))
print(my_func(10,20,lambda a,b: a/b))

def average(list):
    sum=0
    count = 0
    for i in list:
        sum = sum+i
        count+=1
    return sum/count
list1 = [1 ,2,3,5,6,7,4,5,9]
print(average(list1))

def calculate_rectangle_area(length, width):
    return length * width


def calculate_composite_area(a, b, c, d):
    area1 = calculate_rectangle_area(a, b)
    area2 = calculate_rectangle_area(c, d)
    return area1 + area2


result = calculate_composite_area(3, 4, 5, 6)
print(result)

student = ['小美',23,'女']
name,old,gender = student
print(f'name:{name},old:{old},gender:{gender}')

scores = [80, 90, 85, 95, 70]


def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    total_score = calculate_total(scores)
    return total_score / len(scores)


total = calculate_total(scores)
average = calculate_average(scores)
print(f"学生的总成绩为: {total}")
print(f"学生的平均成绩为: {average}")

string_list = ["hello", "world", "python"]
transform = lambda a: [i.upper() for i in a]
result = transform(string_list)
print(result)
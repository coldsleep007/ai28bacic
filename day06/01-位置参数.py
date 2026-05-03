# # 1. 定义函数 user_info(), 接收三个参数, 打印自己的信息: name, age, address
# def user_info(name, age, address):
#     print(f'我叫: {name}, 今年 {age} 岁了, 我住在: {address}')
#
#
# # main函数是程序的 主入口, 所有的代码都是从这里开始执行的.
# if __name__ == '__main__':
#     # 2. 调用函数 user_info()
#     user_info('张三', 23, '北京')
#     user_info('张三', '北京', 23)   # 不报错, 但是结果不是我们要的.
#     #user_info(name = '王五', '深圳', age=25)

def fun(name='小耿', age=18, score=0.000):
    print(f'学生姓名:{name},年龄:{age},成绩:{score:.2f}')


def fun1(*args):
    print(type(args))
    print(f'学生姓名:{args[0]},年龄:{args[1]},成绩:{args[2]:.2f}')


def fun2(**kwargs):
    print(type(kwargs))
    print(f'学生姓名:{kwargs['name']},年龄:{kwargs['age']},成绩:{kwargs['score']:.2f}')


fun('小明', 18, 36.254)
fun(age=18, name='小红', score=69.367)
fun('小西', score=86.789, age=18)
fun()

fun1('小花', 18, 88.479)
fun2(name='小曲', age=18, score=88.479)

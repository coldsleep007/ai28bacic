"""
异常介绍:
    概述:
        在Python中, 我们把程序出现的所有的 非正常情况, 统称为: 异常. 俗称叫: Bug
    常见的异常:
        FileNotFoundError
        除零错误
        ......
    异常的默认处理方式:
        程序会将异常的 类型, 产生原因, 异常出现的位置 打印到控制台上.
        并终止程序的执行.

"""
# 需求: 演示 try.except写法.
try:
    print("try 1")
    # 1. 读取了1个不存在的文件.
    src_f = open('1.txt', 'r')      # FileNotFoundError
    print("try 2")
except:
    print('文件不存在, 请校验后重新操作!')

# 2. 除零异常.
# print(10 // 0)                    # ZeroDivisionError
print('看看我执行了吗?')
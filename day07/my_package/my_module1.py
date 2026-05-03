#自定义的第一个模块

def get_sum(a, b):
    print('我是 my_module1 模块的 函数')
    print(__name__)
    return a + b


def fun01():
    print('我是 my_module1 模块的 函数')
    print('----- fun01 函数 -----')
    print(__name__)


def fun02():
    print('我是 my_module1 模块的 函数')
    print('----- fun02 函数 -----')
    print(__name__)

# 如果条件成立, 说明是在 当前模块中执行的.
if __name__ == '__main__':
    # 测试代码
    print(get_sum(10, 20))
    fun01()
    fun02()
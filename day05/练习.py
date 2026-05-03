# 定义一个简单的函数run，
# 函数的功能是输出"我在跑步" 以及 “管住嘴，迈开腿”，并调用此函数。
# 在第一题中，我们已经用函数run实现了一些功能，
# 如果我们想run函数做的操作执行1000遍，怎么实现代码？

def run():
    print("我在跑步")
    print("管住嘴, 迈开腿")


def multiple(a, b):
    return a * b


def mul(c):
    if c > 1:
        return c * mul(c - 1)
    return c


m = 1


def a():
    global m
    m = 30
    print(m)


if __name__ == "__main__":
    print(multiple(7, 13))
    print(mul(5))
    a()
    print(m)

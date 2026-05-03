def print_info():
    '''

    :return:
    '''

def get_sum(a, b):
    """
    该函数用于计算两个整数和, 并返回求和结果.
    :param a: 要计算的第1个整数
    :param b: 要计算的第2个整数
    :return: 两个整数的求和结果.
    """
    sum = a + b
    return sum

# 2. 调用函数.
result = get_sum(10, 20)

# 3. 打印结果.
print(f'求和结果为: {result}')

def get_sum3(a, b):     # 形参
    """
    该函数用于计算两个整数和
    :param a: 求和计算的第1个整数
    :param b: 求和计算的第2个整数
    :return: 返回求和结果.
    """
    sum = a + b
    return sum


# 调用函数
sum = get_sum3('zz', 'bb')      # 实参
print(f'求和结果为: {sum}')
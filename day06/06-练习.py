"""
定义函数findall，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"
需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
"""


def findall(a):
    b = []
    start = 0
    while True:
        index = a.find('hello', start)
        if index == -1:
            break
        b.append(index)
        start = index + 1
    return tuple(b)


if __name__ == '__main__':
    s = "helloworldhellopythonhelloc++hellojava"
    print(findall(s))

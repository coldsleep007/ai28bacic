"""
捕获异常, 完整格式如下:
    try:
        里边写的是可能出问题的代码
    except [Exception as e]:
        出现问题后的 解决方案
    else:
        只要try中内容无问题, 就会执行这里的内容.
        只要try中有问题, 就会跳过这里的代码.
    finally:
        无论try是否有问题, 都会走这里的内容, 一般用于释放资源.
"""
try:
    src_f = open('1.txt', 'rb')
    des_f = open('2.txt', 'wb')

except Exception as e:
    print(e)
else:
    while True:
        data = src_f.read(1024)
        if len(data) <= 0:
            break
        des_f.write(data)
finally:
    src_f.close()
    des_f.close()
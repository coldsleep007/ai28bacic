"""
注释介绍:用来对程序进行解释
"""
# 注释;
print('hello world!')
flag = True
print(type(flag))
'''
注释
'''
a = 10
b = 20
c = 1235
d = 56
e = 12.36
f = 0.007
print(f'%5d %5d' % (a, b))
print(f'%5d %5d' % (c, d))

print(f'%05d %05d' % (a, b))
print(f'%05d %05d' % (c, d))

print(f'%-5d %-5d' % (a, b))  # -表示左对齐
print(f'%-5d %-5d' % (c, d))

print(f'%0.5f %0.5f' % (e, f))
print(f'%0.5f %0.5f' % (e, f))

print(f'{e:.3f},{f:.3f}')
print(f'{a:6d},{b:6d}')

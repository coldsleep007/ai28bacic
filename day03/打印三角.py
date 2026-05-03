# 1-打印如下图形：
#   *
#  ***
# *****
#  ***
#   *

# 上半部分
for i in range(3):
    spaces = ' ' * (2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# 下半部分
for i in range(1, -1, -1):
    spaces = ' ' * (2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)




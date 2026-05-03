# 扩展: 逻辑运算符操作数字, 小技巧: 你把0当做False, 非0当做True即可.
# 逻辑与操作数字, 结论(技巧): 有0则0(即: 有False则整体为False), 否则取最后1个(非0)数字.
print(10 and 0 and 5)   # 0
print(0 and 3 and 5)    # 0
print(10 and 3 and 5)   # 5
print(0 and 0 and 0)    # 0
print('-' * 28)

# 逻辑或操作数字, 结论(技巧): 有非0则非0(即: 有True则整体为True), 否则取第1个(非0)数字.
print(0 or 0 or 0)    # 0
print(10 or 0 or 5)   # 10
print(0 or 3 or 5)    # 3
print(10 or 3 or 5)   # 10
print('-' * 28)

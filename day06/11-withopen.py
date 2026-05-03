# 备份写法1:
with open(file='./data/numbers.txt', mode='r', encoding='utf8')as read:
    with open(file='./data/number备份.txt', mode='w', encoding='utf8')as write:
        for line in read:
            if line == '':
                break
            write.write(line)

# 写法2:
with open(file='./data/numbers.txt', mode='r', encoding='utf8')as read, open(file='./data/number备份.txt', mode='w', encoding='utf8')as write:
    for line in read:
        if line == '':
            break
        write.write(line)

import os
"""
dirt = input('请输入指定路径：\n')
dir_list = os.listdir(dirt)
for v in dir_list:
    print(v)
"""
"""
# 1.2 输入指定目录和指定文件，判断该文件在目录中是否存在
dirt = input('请输入指定路径：\n')
dir_list = os.listdir(dirt)
file = input('亲输入文件名:\n')
if file in dir_list:
    print(f'文件存在于{os.getcwd()}目录中')

# 1.3 检查【课后作业】目录下，某天哪些同学交了作业，哪么没有交
dirt = input('请输入指定路径：\n')
dir_list = os.listdir(dirt)
print(dir_list)
list1 = ['王志豪', '刘文杰', '黄继豪', '谢心海', '尚光云', '周豪', '晏家栋', '刘文杰', '于越', '陈相泽', '李仲政', '上官思怡', '方星添', '郭兆峰', '谢其志', '余露', '李辉扬', '杨璟', '董志超', '李康辉', '蔡宇轩', '黄锦辉', '苏正辉', '周邦来', '杨程杰', '梁超', '丁少华', '吴振珠', '蒋超', '刘震', '黄天乐', '黄松辉', '陆梓锋', '卿天佳', '段逸', '关鹏程', '欧阳文俊', '杨明姣', '安旭东', '徐文涌', '余炳权', '王国超', '欧阳学良', '吴梦芸', '罗杰', '肖扬', '廖逸儒', '刘欣', '孙容宽', '张震', '杨盛安', '苏海城', '呼嘉欣', '王小铭', '毛培林', '付向杰', '王永豪', '刘子豪']
dir_list = os.listdir(dirt)
print(set(list1) - set(dir_list))
"""
while True:
    try:
        a = input('请输入分子:')
        b = input('请输入分母:')
        print(int(a) / int(b))
    except ZeroDivisionError as e:
        print('发生异常')
    else:
        break
    finally:
        print('程序结束')









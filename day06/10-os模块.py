import os
# os.rename('./data/a.txt','./data/c.txt')  # 文件重命名
# os.remove('./data/b.txt')  # 彻底删除文件,不会进入回收站
# os.mkdir('./data/new.txt')  # 创建新目录
# os.mkdir('./data/a/new.txt')  # 不可以一次创建多级
# os.makedirs('./data/a/new.txt')  # 一次创建多级目录
print(os.getcwd())  # 获取当前文件夹
# ./当前目录 ../上一级目录
os.chdir('../day04')  # 切换目录
print(os.getcwd())  # 获取当前文件夹
print(os.listdir('../day04'))  # 列出当前目录下的所有文件
















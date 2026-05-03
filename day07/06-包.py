"""
包 解释:
    概述:
        包 = 文件夹 = 一堆的.py文件(模块) +  __init__.py 初始化文件.

    背景:
        当我们的模块(.py文件)越来越多的时候, 就要分包来管理它们了(模块).

    导包方式:
        方式1: import 包名.模块名
            必须通过 包名.模块名.函数名() 的方式, 来调用 函数.
        方式2: from 包名 import 模块名
            必须通过 模块名.包名()的形式, 来调用函数.
"""
#import my_module2
import my_package.my_module1

my_package.my_module1.fun01()

from my_package import *
my_module1.fun01()
my_module2.fun01()

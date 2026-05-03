# 案例: 猜拳游戏.
# 需求: 键盘录入玩家出的手势, 且和 电脑人的手势(随机生成), 进行比较, 打印结果.
# 铺垫知识, 如何获取一个指定范围内的随机数.
# 1. 导包, 即: 通过第三方的包来实现.
import random
#print(random.randint(1,2))

# 具体的完成 猜拳游戏案例, 规则: 石头 -> 1, 剪刀 -> 2, 布 -> 3.
# 1. 键盘录入玩家的手势编号, 并接收. 记得转成数值.

player = int(input('亲输入您的手势,石头->1 剪刀->2 布->3'))
pc = random.randint(1,3)
print(f'电脑输出的手势为{pc}')
if (player==1 and pc==2) or (player==2 and pc==3) or (player==3 and pc==1):
    print('玩家胜利\n')
elif player ==pc:
    print('平局\n')
elif(player==2 and pc==1) or (player==3 and pc==2) or (player==1 and pc==3):
    print('电脑胜利\n')

# 需求：根据考试成绩发放奖励，键盘录入小明的考试成绩并接收, 根据考试成绩发放奖励.
# 接收小明的考试成绩
score = int(input("请输入小明的考试成绩（0-100）："))

# 判断成绩是否合法
if score < 0 or score > 100:
    print("输入的成绩不合法，请输入 0 到 100 之间的数字！")
else:
    # 根据成绩发放奖励
    if score >= 90:
        print("小明获得奖励：一台游戏机！😊")
    elif score >= 80:
        print("小明获得奖励：一个书包！😁")
    elif score >= 70:
        print("小明获得奖励：一本习题册！👍")
    elif score >= 60:
        print("小明没有获得奖励，鼓励继续努力！😶")
    else:
        print("小明的成绩不及格，需要叫家长。😫")

# 需求：上述猜拳案例无法实现计算机自动随机出拳。在原有的功能基础上，
# 实现计算机随机出拳。增加游戏趣味性

import random
# 定义选项及其对应名称
options = ["剪刀", "石头", "布"]

# 用户输入
user_choice = input("请输入你的选择（0：剪刀，1：石头，2：布）：")

# 判断用户输入是否合法
if 0 > int(user_choice) or int(user_choice) > 2:
    print("输入不合法，请输入 0、1 或 2！")
else:
    user_choice = int(user_choice)
    # 计算机随机出拳
    computer_choice = random.randint(0, 2)

    # 输出双方出的拳
    print(f"🫠你出了：{options[user_choice]}")
    print(f"🤖AI小智出了：{options[computer_choice]}")

    # 判断胜负
    if user_choice == computer_choice:
        print("平局！")
    elif (
        (user_choice == 0 and computer_choice == 2) or  # 剪刀赢布
        (user_choice == 1 and computer_choice == 0) or  # 石头赢剪刀
        (user_choice == 2 and computer_choice == 1)     # 布赢石头
    ):
        print("😜恭喜，你赢了！")
    else:
        print("😒很遗憾，你输了。")

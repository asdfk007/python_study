# random模块--生成一个随机数

# player，和ai两个玩家
# 0代表石头，1代表剪刀，2代表布
# 1.玩家获胜情况：p0，a1；p1，a2；p2，a0
# 2.玩家电脑平局：p==c
# 3.否则电脑获胜

import random


while True:
    ai = random.randint(0, 2)
    try:
        player = int(input("请输入一个数字，0代表石头，1代表剪刀，2代表布"))
        if (player == 0 and ai == 1) or (player == 1 and ai == 2) or (player == 2 and ai == 0):
            print(f'AI出的是{ai}，玩家胜利')
        elif player == ai:
            print(f'AI出的是{ai}，平局')
        else:
            print(f'AI出的是{ai}，AI胜利')
    except ValueError:
        print("输入有误")

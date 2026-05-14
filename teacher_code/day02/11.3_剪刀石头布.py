# 引入 名为random的 包
import random # 导包

# 电脑随机出 1：石头  2：剪刀 3：布
# 随机返回 1-3 中的一个数字
computer = random.randint(1,3)
print(computer)

# 玩家出 1：石头  2：剪刀 3：布
player_str = input('请输入1、2、3中的一个数字，1表示石头，2表示剪刀，3表示布：')
player = int(player_str) # 输入str 转 int

# 比较谁赢了 输出输赢结果
# 电脑 - 玩家 ==> 5种结果 分别判断即可
if computer - player == 0:
    print('平局！')
elif computer - player == -1 or computer - player == 2:
    print('电脑胜！')
# elif computer - player == 2:
#     print('电脑胜！')

else:
# elif computer - player == -2 or computer - player == 1:
    print('玩家胜利！')
# elif computer - player == 1:
#     print('玩家胜利！')

# print(computer)
# print(f'电脑出的是{computer}，你出的是{player}')



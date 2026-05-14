# 引入 名为random的 包
import random # 导包

# 电脑随机出 1：石头  2：剪刀 3：布
# 随机返回 1-3 中的一个数字
computer = random.randint(1,3)
print(computer)

# 玩家出 1：石头  2：剪刀 3：布
player_str = input('请输入1、2、3中的一个数字，1表示石头，2表示剪刀，3表示布：')
player = int(player_str) # 输入str 转 int

# 电脑 - 玩家
ret = computer - player

# 2 - 1 = 1

if ret == 0:
    print('平局！')
else:
    # if ret == -1 or ret == 2:
    #     result = '电脑胜！'
    # else:
    #     result = '玩家胜！'
    # 等同于下面的一行代码
    # todo =后边：if条件成立，就是if前边的值，不成立就是else后边的值！
    # todo 不管是哪个值，给result这个变量赋值！
    # 等号右边的是一种语法糖：判断推导式
    # 大家都叫下边一行代码为 三元运算
    result = '电脑胜！' if ret == -1 or ret == 2 else '玩家胜！'

print(result)









# 定义一个有参函数，计算并打印两个数字之和
#
# def sumab(a,b):
#     '''
#     计算两个数值的和，打印输出
#     :param a: 形参，int
#     :param b: int
#     :return:
#     '''
#     ret=a+b
#     print(ret)
#     return ret
#
#
# print(sumab(10, 20))
#
#
# #计一个函数求三个数的和
# def sum3(a,b,c):
#     ret=a+b+c
#     print(ret)
#
# sum3(10,20,30)
import random


# 5.1example of function
#
def caiQuanGame(nums, is_player=True):
    """ 猜拳一次
     1：石头； 2：剪刀； 3：布
     电脑-玩家 = 共5种结果
         0：平局
         -1、2：电脑胜
         1、-2：玩家胜
     :param: is_player: 是否由电脑帮玩家猜拳, 默认True, 由玩家输入
             nums: 游戏次数，在本函数中没用，传出函数
     :return: (nums, result_str) ：result_str: 平局！ or 电脑胜！ or 玩家胜！
     """
    computer_int = random.randint(1, 3)
    if is_player:
        player_str = input('1.石头  2.剪刀  3.布 \n玩家请输入')
        player_int = int(player_str)
    else:
        player_int = random.randint(1, 3)

    # 相减
    ret = computer_int - player_int

    if ret == 0:
        result_str = '平局！'
    else:
        # 如果 -1或2 就是电脑胜；除此以外（1或-2；0已经在外层if中判断了）就是玩家胜
        result_str = '电脑胜！' if ret == -1 or ret == 2 else '玩家胜！'
    return nums, result_str


def main():
    num = int(input('输入游戏次数'))
    is_player = input('是否自动进入游戏？y/n')
    is_player_bool = True if is_player == '是' else False
    i = 1
    while True:
        # todo 调用猜拳函数
        result = caiQuanGame(is_player=is_player, nums=num)
        # 输出 caiQuanGame 函数的 第二个返回值 result_str
        print(result[1])  # return (nums, result_str)


        i += 1
        if i > num:
            break
        print('游戏结束')

# 执行程序的主逻辑
main()

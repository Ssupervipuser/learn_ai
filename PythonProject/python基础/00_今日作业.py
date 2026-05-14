import random

# 作业1  05_买苹果案例

# apple_price=input('please input apple price yuan/kg')
# apple_num=input('please input apple number kg')
# apple_amount=float(apple_price)*float(apple_num)
# print(f'apple price {apple_price}yuan/kg, apple number {apple_num}, apple price is {apple_amount}')


# 作业2  设计一个代码，证明 not and or 的先后执行顺序
#     提示：可以两两判断得到先后顺序
# print(False and False or True) #True 证明and比or先执行
# print(False and False)
# print(False and True)
# print(False or True )

# print(not False)
# print(not True)
# print(not False and True)#True 证明 not比and先执行



# 作业3  多分支 09_判断3
#1.接收节日的输入
holiday_name=input("input holiday name")

#2.判断条件1 情人节买玫瑰
if holiday_name=='velentine\' day':
    print("buy rose")

#3.判断条件2 平安夜 买苹果
elif holiday_name=='christmas eve':
    print('buy an apple')
#4. 判断条件3生日买蛋糕
elif holiday_name=='brithday':
    print("buy cake")
#都不符合打印啥也不买

print('起飞')

# 作业4  石头剪刀布！ 请写出两种方式！
# while True:
#     # computer=(random.randint(1,3))
#     computer=3
#     print(computer)
#
#     player=int(input('请输入你的选择---石头1 ，剪刀2，布3：'))
#
#     if computer==player:
#         print('平手')
#     elif computer==1 and player==2 or computer==3 and player==1:
#         print('电脑赢')
#     elif computer==2 and player==3 :
#         print('电脑赢')
#     else:print('选手赢')

while True:
    computer=random.randint(1,3)
    player=int(input('请输入你的选择---石头1 ，剪刀2，布3：'))

    if computer-player==0:
        print('电脑赢')

    elif computer-player==-1:
        print('电脑赢')
    elif computer-player==2:
        print('电脑赢')
    else:
        print('选手赢')

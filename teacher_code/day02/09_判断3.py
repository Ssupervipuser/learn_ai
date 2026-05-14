# 1. 接收节日的输入
holiday_name = input('输入节日名字：')

# todo 3个条件按顺序，只要有一个符合，就立刻执行，剩余的就不执行了！
# todo else表示 3个条件都不满足的时候，就执行else中的代码
# 2. 判断 条件1 情人节 买玫瑰
if holiday_name == '情人节':
    print('买玫瑰')
# 3. 判断 条件2 平安夜 买苹果
elif holiday_name == '平安夜':
    print('买苹果')
# 4. 判断 条件3 生日 买蛋糕
elif holiday_name == '生日':
    print('买蛋糕')
# 5. 都不符合，打印 啥也不买
else:
    print('啥也不买')

"""
# 2. 判断 条件1 情人节 买玫瑰
if holiday_name == '情人节':
    print('买玫瑰')

# 3. 判断 条件2 平安夜 买苹果
if holiday_name == '平安夜':
    print('买苹果')

# 4. 判断 条件3 生日 买蛋糕
if holiday_name == '生日':
    print('买蛋糕')
# 5. 都不符合，打印 啥也不买
else:
    print('啥也不买')

上边3个if彼此是独立的！
最后一个else和它前边的最近的if是一起的！  
"""
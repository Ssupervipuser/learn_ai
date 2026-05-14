# todo 这是作业！
# 从键盘上录入苹果的价格 、重量 ，
# 输出: 苹果单价 XXX 元/斤，购买了 XXX 斤，需要支付 XXX 元.
# input接收的是str!

# 1. 定义变量：苹果单价
# input(n) 是个函数, n是能够在输出界面展示出来的，在n的后边让我去通过键盘去输入，回车结束
# price_str 是我自己起的名字，表示苹果的单价，类型是字符串
price_str = input('请输入苹果的单价：')

# 2. 定义变量：XXX斤
num_str = input('输入购买的斤数（数量）：')

# todo 3. 将 苹果单价、数量两个变量的值从str字符串转换为int或float数字类型
price_float = float(price_str)
num_float = float(num_str)

# 4. 定义变量：支付的总金额 = 苹果单价 * XXX斤
price_total = price_float * num_float

# 5. 打印输出所有变量
# 第1种方式
print(
    '苹果单价 %d 元/斤，购买了 %f 斤，需要支付 %s 元.' %
    (price_float, num_float,price_total)
)
# 第2种方式
print(
    '苹果单价 {} 元/斤，购买了 {} 斤，需要支付 {} 元.'.format(
        price_str,
        num_str,
        price_total
    )
)

print(
    '苹果单价 {price} 元/斤，购买了 {num} 斤，需要支付 {price_total} 元.'.format(
        price = price_str,
        num = num_str,
        price_total = price_total
    )
)

# 第3种方式
print(
    f'苹果单价 {price_str} 元/斤，购买了 {num_float} 斤，需要支付 {price_total} 元.'
)


# 如果我想让input接收 n ，同时在终端输出 【苹果的单价是 n 元/kg】
# input('苹果的单价是 ')
# print(' 元/kg')
a = input()
print('苹果的单价是 {} 元/kg'.format(a))
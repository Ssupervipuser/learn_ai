# 匿名函数 lambda函数 lambda表达式

# 正常函数的样子
def func(a, b):
    return a + b
print(func(1,3))

# lambda函数有名字的用法
lambda_func = lambda a,b: a+b
res = lambda_func(1,3)
print(res)

# lambda函数没名字、直接调用的方法
print(
    # lambda 关键字，表示后边要定义匿名函数
    # 冒号前边 a, b 形式参数
    # 冒号后边 a + b 函数的运行过程、同时也是该匿名函数的返回值
    (lambda a,b: a+b)(a=1, b=3)
    # (lambda a,b: a+b) 就是匿名函数的整体，加小括号目的是要执行调用
    # (a=1, b=3) 就是传参
)

# todo 冒号右边即是函数的内容、又是函数的返回值
lambda_func2 = lambda : print('没参数')
lambda_func2()

# 需求：写一个匿名函数，求a的平方 a**2
# lambda 参数: 运行过程、返回结果
# lambda a: a**2

# 1. 没有名，直接调用传参执行
print((lambda a: a**2)(a=10))

# 2. 起个名，调用传参执行
lambda_func3 = lambda a: a**2
# 用一个变量名接收这个匿名函数运行的结果
ret = lambda_func3(10)
print(ret)

# def func(a):
#     return a**2
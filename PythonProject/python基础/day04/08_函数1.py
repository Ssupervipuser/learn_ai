

# 自定义函数
def sum_a_b():
    """
    计算1+2的结果，打印输出
    :return:
    """
    a = 1
    b = 2
    ret = a + b
    print(ret)
sum_a_b()

print('*'*5)

# 定义一个函数，能够计算并打印出两个数字之和。
def sum_a_b(a, b):
    """
    计算两个数值的和，打印输出
    :param a: 形参，int类型
    :param b: 形参，int类型
    :return:
    """
    ret = a + b
    # print(ret)
    return ret # return返回 返回ret这个变量的值

# 调用函数，传入的数字2、3就是实参
result = sum_a_b(2, 3)
print('*'*5)
print(result)

# todo 函数如果没有return，或return后边没有任何东西
# todo 该函数返回 None
def func1(a, b):
    ret = a + b
    return # 还表示终止函数、函数结束了！
    print('这是另外一种注释的形式吧') # 这里永远不会被执行
    print(33333) # 这里永远不会被执行
print(func1(1, 2)) # None

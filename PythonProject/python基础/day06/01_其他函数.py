
lst = [i for i in range(1,11)]
lst = [1, 2, 3, 4, 5,
       6, 7, 8, 9, 10]

def func(i):
    """
    判断函数
    :param i: 传入的一个数字
    :return: True 或 False
    """
    return i % 2 == 1

# todo 1. filter函数：对传入的第2个参数（列表），基于第一个参数（函数名）进行过滤
# todo 第一个参数是函数名，该函数返回True或False
# todo True时传入的那一个遍历出来的元素保留
res = filter(func, lst)
print(list(res))

# filter函数中第一个参数可以用lambda
res = list(filter(lambda i: i%2==1, lst))
print(res)

# 下面列表中的数字变正数：filter函数实现不了！
lst2 = [-5, 3, -7, -99, 8, -9]
def func1(i):
    if i > 0:
        ret = i
    else:
        ret = -i
    print(ret)
    return ret

lst3 = list(filter(func1, lst2))
print(lst3)

# todo filter函数只干过滤的事儿！不能做处理数据的事儿！
# 将列表中所有正数取出，负数不要了
lst2 = [-5, 3, -7, -99, 8, -9]
def func2(x):
    # 返回真或假
    if x > 0:
        return True
    else:
        return False
def func2(x):
    # 返回真或假
    return True if x>0 else False

# 写成lambda
# lambda x: True if x>0 else False

res = list(filter(func2, lst2))
print(res)

res = list(filter(lambda x: True if x>0 else False, lst2))
print(res)


# todo 2.map函数：对每一个元素执行指定函数
# todo 该函数的返回值构成新可迭代对象
# todo map第一个参数是函数，一共执行len(lst)次
# 把一个全是数字的列表中每个元素都计算平方，组成新列表
lst = list(range(10)) # 列表 0-9
ret = list(map(lambda i: i**2, lst))
print(ret)

# 需求：把负数全变成正数，返回新列表
lst2 = [-5, 3, -7, -99, 8, -9]
# 1. 定义函数，将传入的每个元素判断正负，正数不变、负数改正数
def func(i):
    # if i > 0:
    #     return i
    # else:
    #     return -i
    return i if i>0 else -i
func = lambda i: i if i>0 else -i
# 2. map函数+list函数，返回新的全是正数的列表
res = list(map(func, lst2))
print(res)

# todo reduce函数
# 需求：计算1-100的和，reduce函数实现
from functools import reduce
def func(x, y):
    # 计算第一个元素 + 第二个元素，返回计算结果
    # 上一次计算结果 + 第三个元素，返回计算结果
    # ...
    # 上一次计算结果 + 最后一个元素，返回计算结果
    return x + y
func = lambda x, y: x+y
lst = list(range(1, 101))
# 1-100的和 = reduce(函数, [1-100])
"""
将lst中前2个元素，传入func函数，该函数得到一个结果
这个结果、第3个元素，再传入func函数，得到一个新的结果
新结果、第4个元素，再传入。。。直到最后一个元素
"""
res = reduce(func, lst)
print(res)

# num = 3
# ret = list(range(num, 0, -1))
# print(ret, '<------')
# 需求：写个函数 使用reduce和lmabda实现阶乘
from functools import reduce
def func(num):
    # 定义列表
    # ret = list(range(num,0,-1))
    # print(ret)
    # lambda 实现对传入的每一个元素进行乘法、返回结果
    res = reduce(lambda x, y: x * y, list(range(num,0,-1)))
    return res
print(func(num=5), '<------计算阶乘')
"""
filter函数： new_lst = list(filter(过滤函数, lst))
    过滤：根据过滤函数的逻辑对lst中每一个元素进行过滤
    过滤函数只返回True或False，True表示该元素被保留
map函数：new_lst = list(map(处理函数, lst))
    逐一处理每一个元素：每一个元素都传入处理函数
    根据处理函数的逻辑，返回新的值，构成新的可迭代对象，最终转成列表
functools.reduce函数：result = reduce(处理函数, lst)
    逐一对每一个元素进行重复处理，最终返回一个结果
    处理函数的逻辑是第1个元素和第2个元素作为参数，一起得到一个结果
    这个结果和第3个元素作为参数再通过处理函数得到新的结果
    直到最后
"""


# todo round函数：处理小数的位数
num = 3.9415926575
ret = round(num) # 把小数变成整数、小数点后边四舍五入
print(ret)

num = 3.9415926575
ret = round(num, 2) # 保留2位小数、小数点后边四舍五入
print(ret)

# 需求：把列表中所有数字，全部按四舍五入变成3位小数
lst = [0.34567, 1.6568596859, 0.21782121]

lst2 = [round(i, 3) for i in lst]
print(lst2)

lst2 = list(map(lambda i:round(i, 3), lst))
print(lst2)
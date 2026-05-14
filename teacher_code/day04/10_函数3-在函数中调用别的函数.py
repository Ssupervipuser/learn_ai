
# 设计一个函数求三个数的和
def sum_3_num(a,b,c):
    # 求三数的和
    return a + b + c

print(sum_3_num(10,2,3))


# 设计一个函数，求三个数的平均数
# 平均值 = 几个数的和 / 个数
def avg_3_num(a,b,c):
    sum_3 = a + b + c
    avg_3 = sum_3 / 3
    return avg_3
print(avg_3_num(1,2,3))


# 在函数中调用其他函数
def avg_3_num(a,b,c):
    # todo 在函数中调用其他函数，参数可以直接传递
    sum_3 = sum_3_num(a,b,c)
    avg_3 = sum_3 / 3
    return avg_3
print(avg_3_num(1,2,3))

# 代码再少写点
def avg_3_num2(a,b,c):
    return sum_3_num(a,b,c) / 3

print(avg_3_num2(12,2,3))
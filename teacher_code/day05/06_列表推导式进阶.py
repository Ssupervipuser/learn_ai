

lst = [i for i in range(10)]
print(lst)

# todo if条件成立时，i被添加到列表中
lst = [i for i in range(10) if True]
print(lst)
lst = [i for i in range(10) if False]
print(lst)


# 需求：列表推导式，构成偶数列表，从2到10，不许用range步长
lst = [
    i for i in range(2, 11)
    if i % 2 == 0 # 条件成立时，i才会被保留
]
print(lst)

"""
[i*2 for i in ....]
[i*2 for i in ... if 条件] # 条件成立i才保留
"""

# 练习：求1-100中所有奇数的和
# 列表推导式，range不让用步长
lst = [
    i for i in range(1, 100)
    if i % 2 == 1 # 条件成立时，i才会被保留
]
print(sum(lst))
# print(lst)
# res = 0
# for i in lst:
#     res += i # res = res + i
# print(res)


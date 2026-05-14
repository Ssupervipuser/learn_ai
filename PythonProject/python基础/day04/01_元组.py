

# 定义一个元组
a = (1)  # 这是个int！
b = (1,)
c = (1,2,3)

# <class 'int'> <class 'tuple'> <class 'tuple'>
print(type(a), type(b), type(c))

# 下标
print(c[0], c[-1])
print(c[::-1])

# 可遍历
for i in c:
    print(i)

# len(c) 计算元组中元素的个数
# 元组中的元素得能够进行计算，才能求max min sum
print(len(c), max(c), min(c), sum(c))

# 判断元素是否在元组中
if 5 in c:
    print('5在里边')
elif 5 not in c:
    print('5不在c元组中')
else:
    print(1111)

# 同时遍历元组的下标和元素的值
for i, v in enumerate(c):
    print(i, v)

# todo 元组不能增删改！其他跟列表一样
c[0] = 55
print(c)
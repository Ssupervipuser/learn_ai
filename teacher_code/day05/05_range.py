
# todo range(10) 返回一个可遍历对象
# todo 从0-9数字中每次遍历返回一个数字
for i in range(10):
    print(i)

print('*'*5)
# 要求遍历打印输出 6-10
# range(6, 11) 表示 6-10
for i in range(6, 11):
    print(i)

print('*'*5)
for i in range(1,11,2):
    print(i)
# range(1,11,2) 从1开始包括1，到11结束不要11，步长为2

print('*'*5)
for i in range(1,-11,-1):
    print(i)
# todo range(x,y,z) x,y,z和切片用法一样

# 需求1：for循环计算1-100（左右都包含）的和，要求用range
sum_1_100 = 0
for i in range(1, 101):
    sum_1_100 += i
print(sum_1_100)

# 需求2：for循环计算1-100（左右都包含）的【偶数】和，要求用range
sum_2_100 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_2_100 += i
print(sum_2_100)

sum_2_100 = 0
# range(2, 101, 2) 第一个2表示从2开始包括2
# range(2, 101, 2) 101表示到101结束不要101
# range(2, 101, 2) 最后的2表示 步长为2（【2,3,4...】3不要了）
for i in range(2, 101, 2):
    sum_2_100 += i
print(sum_2_100)
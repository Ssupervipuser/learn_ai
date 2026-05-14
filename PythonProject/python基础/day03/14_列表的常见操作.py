
my_list = [1,2,3,4]
print(my_list)

# 1. 列表在最右边添加元素 list.append(x)
my_list.append(5) # 列表中从右边添加元素：数字1
print(my_list)
# my_list = [1]
# print(my_list, type(my_list))

# 2. 删除列表中的元素：list.remove(x) ，x是要删除的元素
my_list.remove(3)
print(my_list)

# 3. 修改列表中的值
# 通过列表的下标 重新赋值 ，从而修改指定下标元素的值
my_list[1] = 22
print(my_list)


# 4. 计算列表元素的个数
print(len(my_list))


# 5. 判断元素是否在列表中
# x in list
print( 4 in my_list ) # True
# 4 in my_list 就是一个 条件表达式
if 4 in my_list:
    print('存在该元素')
# x not in list
print( 4 not in my_list ) # False

ret = my_list.sort()
print(ret) # None

# 列表.sort() 对列表进行升序排列，原列表就被改变了
# 列表.sort() 没有返回值
my_list.sort()
print(my_list)

# 列表.sort(reverse=True) 降序！
# 列表.sort() 默认是升序！ reverse=False
my_list.sort(reverse=1)
my_list.sort(reverse=True)
print(my_list)
my_list.sort(reverse=0)
print(my_list)


# 列表自己的函数方法，直接操作列表、没有返回值
# 直接对原列表进行增、删、排序三种修改，原列表发生了改变！
"""
my_list = [元素1, ...] # 定义一个列表
my_list.append(1) # 增
my_list.remove(1) # 删
my_list.sort() # 排序
my_list[下标] = 新的值 # 改
my_list[下标]  # 查
for i in my_list: # 查，遍历列表
    print(i) 
"""


# my_list = [1,2,3,4]
# my_list2 = my_list
# my_list2.append(5)
# print(my_list, my_list2)


# 常见的几种情况1
my_list = [1,2,3,4]
print(my_list.sort(reverse=1)) # None 没有返回值
print(my_list)

# 常见的几种情况2
my_list = ['1','2','3','中国']
my_list.sort(reverse=1) # 可以排序
print(my_list)

# 常见的几种情况3：报错！
# my_list = ['1','2','3','4', 88]
# my_list.sort() # 不能排序！
# print(my_list)

# 补充1：通过下标删除列表中的元素
my_list = [1,2,3,4]
del my_list[-1] # -1是右边第一个元素的下标，删除它
print(my_list)

# 补充2：求列表中最大值、最小值、求元素值的和
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print('*'*5)

# 下边的操作 别做！
# my_list = ['1','2','3','中国']
# print(max(my_list)) # 中国
# print(min(my_list)) # 1
# print(sum(my_list)) # 报错

# 反转元素的顺序，倒序，不改变原列表
my_list = [1,2,4,3]
print(my_list[::-1]) # [3, 4, 2, 1]
print(my_list)

# 获取列表反转元素之后的新列表
new_list = my_list[::-1]
print(new_list)
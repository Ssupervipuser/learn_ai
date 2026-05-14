
# 1. 串讲笔记中 3.3.1 循环嵌套
# 2. 串讲笔记中 3.3.2 break和continue
# 3. 代码 12_for循环
# 4. 列表相关内容
# 附加题： 看代码17_切片！


# todo while循环:重复执行代码块
i = 1
# 外层循环 控制行数
while i <= 5:
    j = 1
    # 内层循环 控制单行中打印星号的次数
    while j <= i:
        print('*', end='') # end='' 不换行
        j += 1
    print() # 强制换行
    i += 1

i = 1
while True:
    # 判断是否到6
    if i == 6:
        print('跳过6')
        i += 1 # 在本次循环结束之前 i 要自增 1
        continue # 提前结束本次循环，继续下一次循环
    print(i)
    i += 1
    # 判断 i 超过10
    if i > 10:
        break # 结束全部循环
print('while循环之后的代码')

# todo for循环：遍历字符串、列表
# 遍历字符串中每个字符
for i in '12哈a……%@':
    print(i)

# 任意输入字符串，找到第一个数字字符并输出
my_str = input('任意输入字符串：')
for i in my_str:
    # 判断每一个字符是否在 '1234567890'中
    if i in '1234567890':
        print(i)
        break


# todo 列表
"""
my_list = [元素1, ...] # 定义一个列表
my_list.append(x) # 从右边末尾添加元素x
my_list.remove(x) # 删除元素x 
my_list.sort() # 排序 默认升序
my_list.sort(reverse=1) # 排序 降序
my_list[下标] = 新的值 # 通过下标来修改指定元素的值
my_list[下标]  # 通过下标去查

# 查，遍历列表每一个元素的值
for i in my_list: 
    print(i)
    
 # 查，遍历列表每一个元素的下标、元素的值   
for i,v in enumerate(my_list):
    # i 就是下标 v 是值
    print(i, v)
"""

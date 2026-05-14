
print('"') # 输出 双引号 这个字符串
print("'")

my_float = 3.5415926
print(my_float)
# todo round() 内置函数，控制小数的位数
new_float = round(my_float) # 去掉所有小数，四舍五入
print(new_float)
new_float2 = round(my_float, 2) # 保留2位小数，四舍五入
print(new_float2)

bool_1 = True
bool_2 = False

# True就是1
if bool_1 == 1:
    print('True就是1')
# False就是0
if bool_2 == 0:
    print('False就是0')

# None
print(None) # 可以输出 None
print(type(None)) # <class 'NoneType'>

print(str(11111)) # 转字符串
print(str(True), str(False))

# 5.0 、 1.0 、 0.0
print(float(5), float(True), float(False))
# 12345 1 3
print(int('12345'), int(True), int(3.64))

# todo 小数转整数的时候，位数的处理
# int(3.14)  int(3.64)  ==> 舍弃小数
# round(3.14) round(3.64)  ==> 四舍五入

# 输入
# print(
#     type(input('接收的一切都是字符串：'))
# )

# todo 格式化输出的三种方式
# 第1种方式
# %s 字符串
# %d 整数
# %.nf 表示 保留n位的小数，四舍五入
a = '%s, %d, %.2f' % ('小明', 18, 3.13556666)
print(a)

# 第2种方式，使用 字符串.format() 函数
# 字符串.format() ==>  字符串的format函数
b = '{}, {}, {}'.format('小明', 18, round(3.13556666, 2))
print(b)


# 第2种方式，使用 字符串.format() 函数，并指定变量名
b = '{name}, {age}, {num}'.format(
    num = '1111.111',
    name = '小明',
    age = 19
)
print(b)

# 第3种
name, age, num = '小明', 19, 1.215111
# f'字符串' 的f是前缀声明，声明的是：后边大括号里我要做变量名填空了！
# {num:.2f} 表示 传入num这个变量，同时小数点后边保留2位、四舍五入
c = f'{name}, {age}, {num:.2f}'
print(c)

# todo 格式化输出 对比
a = '%s, %d, %.2f' % ('小明', 18, 3.13556666)
b1 = '{}, {}, {}'.format('小明', 18, round(3.13556666, 2))
b2 = '{name}, {age}, {num}'.format(
    num = '1111.111',
    # name = '小明',
    name = True,
    age = 19
)
c = f'{name}, {age}, {num:.2f}'


# 符合赋值运算
a = 0
a += 1  # ==> a = a+1
# 永远都先执行计算 等号 右边，再去执行等号和等号左边

"""判断
if 条件表达式 or 条件:
    # 如果条件表示为True，就执行下边的代码A
    代码A ...
elif 条件表达式:
    代码B
else:
    代码C      
"""

# todo 条件表达式，是个bool类型、真假值
print(
    5==5,  # 输出True，==表示比较左右两边的值是否相等
    5!=6,  # 输出True，!=表示比较左右两边的值是否【不】相等
    True and False, # and表示比较两边的真假值，全真为真
    True or False, # or比较两边的真假值，全假为假
    not True # False，not表示取反值
)
# todo 三者执行的顺序：not and or
print(5 == 5 or 5 >= 6 and 5 != 6)
print(((5 == 5) or (5 >= 6)) and (5 != 6))

if True:
    print(111)
if 1:
    print(222)
if 0: # 永远不成立的条件
    print(333)
if -1:
    print(444)

abc = '字符串'
if abc:
    print(abc)
abcd = ''
if abcd: # 空字符串作为条件时，判断的条件永远不成立
    print(555)
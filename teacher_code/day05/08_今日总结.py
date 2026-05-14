# 1. 函数的不定长参数
def func(a, b, *args, c=1, **kwargs):
    # a, b 叫做普通参数
    # *args 元组不定长参数
    # c=1 默认值、缺省参数
    # **kwargs 字典不定长参数
    print(a, b)
    print(*args) # 拆包
    print(args) # 一个元组
    print(c)
    print(*kwargs) # 拆包拆出来两个key
    print(kwargs) # 一个字典

func(
    1,
    2,
    3,
    4,
    5,
    6,
    c=7,
    d=8,
    f=9
)

# 2. 组包与拆包
a, b = 1, 2
# 1,2 ==> (1,2)
# ab = (1,2)
# a,b = (1,2)
a, b = b, a
# b, a ==> (b, a)
# ab = (b, a)
# a, b = (b, a)

def func(a,b):
    return a,b
print(func(1, 2)) # (1, 2)
a, b = func(1,2)
print(a,b)
print(func(1, 2)[0]) # 1

for i, (k, v) in enumerate({'a':1, 'b':2, 'c':3}.items()):
    print(i, k, v)

# 3. 可变不可变
# 一个容器中元素变了，但容器不变，就是可变类型
# 一个容器中元素id变了，但这个容器id不变，就是可变类型
a = [1, 2, 3]
print(id(a))
# a.append(4)
a[0] = 5
print(id(a))
# 可变：列表、字典、集合
# 不可变：字符串、元组、数字

# 4. 深浅拷贝
# todo 浅拷贝管不了嵌套的情况
lst1 = [[1,2], 3, 4, 5]
lst2 = lst1.copy()

print(lst1, id(lst1))
print(lst2, id(lst2))
lst1[0][0] = 10
print(lst1, id(lst1))
print(lst2, id(lst2))
# todo 所以就用深拷贝
from copy import deepcopy
lst3 = deepcopy(lst1) # 得到深拷贝之后全新的列表

# 5. range函数
"""
range(5) # 0-4
range(1,5) # 1-4
range(1,10,2) # 1、3、5、7、9
range(1,-5,-1) # 1、0、-1、-2、-3、-4
"""
for i in range(10): print(i)

# 6. 列表推导式
lst4 = [i**2 for i in range(10)]
# 0-9数字，能够被2整除余数为0的数字，平方的结果，放入列表中
lst5 = [i**2 for i in range(10) if i % 2 ==0]
# if条件成立时，当次遍历出来的单个对象才会被保留

# 需求：用列表推导式，获取所有能够被3整除的、200以内的整数的3次方
# 1. 列表推导式
# [ for i in ]
# [i for i in 被遍历迭代的对象]
# [i for i in range(100)]
#
# # 2. 200以内整数
# [i for i in range(201)]
#
# # 3. 被三整除
# [i for i in range(201) if 条件]
# [i for i in range(201) if i % 3 ==0]

# 4. 3次方
lst5 = [i**3 for i in range(201) if i % 3 == 0]
print(lst5)

print('*'*5)
# 7. lambda匿名函数
print( (lambda x: x+1)(x=5) )

lambda_func = lambda x, y: x+y
result = lambda_func(x=1, y=2)
print(result)

# lambda匿名函数 起个名
func3 = lambda : print(111)
# func3就是lambda函数的名字，实质func3指向、引用了 lambda函数
# 打印func3输出的是他指向、引用的函数【还没执行呢！没调用呢！】
print(func3) # <function <lambda> at 0x0000025DD7DDD080>
res = func3()
print(res)

def func1():
    # 定义个一个函数，返回值是 222
    return 222
# 给func1函数增加一个名字叫func2
func2 = func1
func2() # 调用func2函数，但不要返回值
# 调用func2函数，获得函数的返回值
res = func2()
print(res)


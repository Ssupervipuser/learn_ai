
# 形参
def func1(a, b):
    pass

# 实参
func1(1, 2)


# 给形参传递实参的两种方式
# 1.按照形参的顺序，依次给于实参
func1(1, 2)
# 2.按形参名字给实参
func1(a=1, b=2)
func1(b=2, a=1)


# todo 形参定义的4种情况、方式
# 1. 普通
def func(a, b):
    print(a, b)

# 2. 缺省【默认】
def func(a, b=1):
    # b=1 表示 b的默认值是1，b这个参数可传可不传
    # 不传为默认值，传谁就是谁
    print(a, b)
func(a=1)
func(a=1, b=3)
# def func(a, b=2, c=3, d=4):pass

# 3. 元组不定长
def func3(*args):
    # todo *args 元组不定长参数
    # 可以接收任意个参数，不指定参数名（形参）
    # *args 把所有参数展开
    print(*args) # 1 2 3
    # args 所有参数按顺序放到元组中
    print(args) # (1, 2, 3)
    print(type(args)) # <class 'tuple'>

func3(1,2,3)
# func3(a=1) 报错！

# 4. 字典不定长
def func4(**kwargs):
    # todo **kwargs 字典不定长参数
    # 可以接收任意个参数，调用传参时必须 参数名=参数值
    # print(**kwargs) 报错！不让这么写！
    print(*kwargs) # name age gender
    print(kwargs) # {'name': '刘海柱', 'age': 18, 'gender': '男'}
    print(type(kwargs)) # <class 'dict'>
    print([v for v in kwargs.values()]) # ['刘海柱', 18, '男']

func4(
    name='刘海柱',
    age=18,
    gender='男'
)

# func4(1,2,3) 报错！不能这么写！

# todo 四种形式的形参同时存在时，严格按照下边的顺序！
# todo 普通参数，元组不定长，默认缺省参数，字典不定长
def func5(a, *args, b='123', **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)

func5(1,2,3,4,5, b='默认值改变',name='刘海柱', age=18)
"""
1
(2, 3, 4, 5)
默认值改变
{'name': '刘海柱', 'age': 18}

"""

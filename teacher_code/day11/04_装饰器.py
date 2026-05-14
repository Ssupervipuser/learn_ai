
#
def comment():
    print('发表评论')

#
def check(fn):
    def inner():
        print('先登录')
        fn() # 函数调用执行
    return inner

inner = check(comment)
inner()
# comment = check(comment)
# comment()

print('*'*10, '装饰器语法糖用法')
def check(fn):
    def inner():
        print('先登录')
        fn() # 函数调用执行 ==> comment()
        print('点赞')
    return inner
# check就是闭包函数
@check
def comment():
    print('发表评论')
comment()
""" 装饰器执行顺序！
1. 先把被装饰的函数名作为参数传入装饰器函数中
2. 装饰器函数执行，返回内部函数名（函数定义）
3. 执行内部函数，在内部函数中、执行了被装饰的函数
    从外部函数的参数获取到了被装饰的函数名
"""


print('*'*10, '被装饰函数，无参数无返回值')
def print_info(func):
    def inner():
        print('努力计算中...')
        func()
    return inner

@print_info
def get_sum():
    a, b = 10, 20
    c = a + b
    print(f'两数和是{c}')

get_sum()

print('*'*10, '被装饰函数，【有】参数无返回值')
def print_info(func):
    def inner(a, b): # todo 在内部函数接收被装饰函数的参数
        print('努力计算中...')
        func(a, b) # 被装饰函数传参执行
    return inner

@print_info
def get_sum(a, b):
    c = a + b
    print(f'两数和是{c}')

get_sum(10, 20)

# 被装饰函数的参数传递的原理
def get_sum(a, b):
    c = a + b
    print(c)
def print_info(fn):
    def inner(a, b):
        print('努力计算中')
        fn(a, b) # 函数调用执行
    return inner
inner = print_info(get_sum)
inner(a=10, b=20)


print('*'*10, '被装饰函数，无参数【有】返回值')
def print_info(func):
    def inner():
        print('努力计算中...')
        result = func() # 被装饰函数有返回值
        return result # todo 内部函数返回被装饰函数的返回值
    return inner

@print_info
def get_sum():
    c = 11 + 22
    print(f'两数和是{c}')
    return c

ret = get_sum()
print(ret)

# 被装饰函数的返回值传递的原理
def get_sum():
    c = 11 + 22
    print(f'两数和是{c}')
    return c
def print_info(func):
    def inner():
        print('努力计算中...')
        result = func() # 被装饰函数有返回值
        return result # todo 内部函数返回被装饰函数的返回值
    return inner

inner = print_info(get_sum)
ret = inner()
print(ret)


print('*'*10, '被装饰函数，【有】参数【有】返回值')
def print_info(func):
    def inner(a, b):
        print('努力计算中...')
        result = func(a, b) # 被装饰函数有返回值
        return result # todo 内部函数返回被装饰函数的返回值
    return inner

@print_info
def get_sum(a, b):
    c = a + b
    print(f'两数和是{c}')
    return c

ret = get_sum(a=13, b=14)
print(ret)

# 被装饰函数的参数和返回值传递的原理
def get_sum(a, b):
    c = a + b
    print(f'两数和是{c}')
    return c
def print_info(func):
    def inner(a, b):
        print('努力计算中...')
        result = func(a, b) # 被装饰函数有返回值
        return result # todo 内部函数返回被装饰函数的返回值
    return inner

inner = print_info(get_sum)
ret = inner(a=13, b=14)
print(ret)


print('*'*10, '通用装饰函')
def print_info(fn):
    def inner(*args, **kwargs):
        print('增加被装饰函数功能的地方1')
        print(args)
        print(kwargs)
        ret = fn(*args, **kwargs)
        print(ret)
        print('增加被装饰函数功能的地方2')
        return ret
    return inner

@print_info
def get_sum(*args, **kwargs):
    result = 0
    for v in args:
        result += v
    for v in kwargs.values():
        result += v
    return result

ret = get_sum(1,2,3,a=4,b=5)
print(ret)

@print_info
def func2(a, b, e=11, f=222, g=66):
    print(22222)
    return a, b, e, f, g
func2(1, 2, e=22, g=66)

# todo 装饰器的作用：不改变被装饰函数，执行被装饰函数时额外增加功能
# todo 装饰器的定义：
#  有嵌套：外层函数中嵌入内层函数
#  有引用：内部函数引用外部函数的变量或参数（被装饰函数名）
#  有返回1：外部函数返回内部函数名（内部函数定义）
#  有返回2：内部函数返回被装饰函数的（加工处理后的）返回值
#  内部函数中执行了被装饰的函数
#  增加功能：内部函数中增加额外的功能代码，就可以扩展被装饰函数的功能
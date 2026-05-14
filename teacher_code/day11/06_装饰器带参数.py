
"""
def decorator(fn, flag):
    def inner(a, b):
        if flag == '+':
            print('正在做加法')
        elif flag == '-':
            print('正在做减法')
        else:
            print('没有在做加减法')
        result = fn(a, b)
        return result
    return inner

@decorator('+') # todo 只能传入一个参数！
def add(a, b):
    return a + b

ret = add(1,3)
print(ret) # todo 报错 原因是 15行注释
"""

# todo 如果装饰器需要额外的参数
#  在原有装饰器函数外边再包裹一层函数
#  最外层的函数接收额外的参数
#  最外层的函数返回第二层函数名
def logging(flag):
    def decorator(fn):
        def inner(a, b):
            if flag == '+':
                print('正在做加法')
            elif flag == '-':
                print('正在做减法')
            else:
                print('没有在做加减法')
            result = fn(a, b)
            return result
        return inner
    return decorator

@logging('+') # todo 只能传入一个参数！
def add(a, b):
    return a + b

ret = add(1,3)
print(ret)
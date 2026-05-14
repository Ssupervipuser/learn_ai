def print_info(fn):
    print('装饰器一旦使用 【@装饰器函数名】，这里就会输出')
    def inner(*args, **kwargs):
        print('增加被装饰函数功能的地方1')
        print(args)
        print(kwargs)
        ret = fn(*args, **kwargs)
        print(ret)
        print('增加被装饰函数功能的地方2')
        return ret
    return inner

@print_info # todo @装饰器 一旦出现 立刻加载外层函数
def get_sum(*args, **kwargs):
    result = 0
    for v in args:
        result += v
    for v in kwargs.values():
        result += v
    return result

# ret = get_sum(1,2,3,a=4,b=5)
# print(ret)

print('*'*10, '多装饰器')
# 装饰器1：模拟输入用户名密码
def up_func(down_func_inner):
    # 传入的参数是 距离较近的内层函数
    print('距离较远的外层函数开始执行')
    def inner():
        print('距离较远的内层函数')
        down_func_inner() # 距离被装饰函数最近的装饰器的内层函数 ==> check_user_inner
    print('距离较远的外层函数结束执行，返回自己的内层函数')
    return inner

# 装饰器2：模拟验证用户名密码
def down_func(comment):
    # 传入的参数是 被装饰的函数
    print('距离较近的外层函数开始执行')
    def inner():
        print('距离较近的内层函数')
        comment() # 被装饰的函数
    print('距离较近的外层函数结束执行，返回自己的内层函数')
    return inner

@up_func # 输入账号密码
@down_func # 验证账号密码
def comment():
    print('被装饰的函数')

comment()

# print('*'*10, '多装饰器的运行原理')
# def comment():
#     print('发表评论')
#
# down_func_inner = down_func(comment)
# up_func_inner = up_func(down_func_inner)
# up_func_inner()
"""
距离被装饰函数较近的内层函数 = 距离被装饰函数较近的外层函数(被装饰函数)
距离被装饰函数较远的内层函数 = 距离被装饰函数较远的外层函数(距离被装饰函数较近的内层函数)
距离被装饰函数较远的内层函数()

1. 运行距离被装饰函数最近的装饰器函数
    把被装饰的函数名作为参数传入
    返回该装饰器函数的内层函数名
2. 运行距离被装饰函数第二近的装饰器函数
    把最近的装饰器函数的内层函数名作为参数传入
    返回该装饰器函数的内层函数名
3. 执行上一步返回的装饰器函数的内层函数
    调用执行了较近的内层函数，该函数又调用执行了被装饰的函数
"""
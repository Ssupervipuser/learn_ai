
def func_out(num1):
    def func_inner(num2):
        # num1是外部函数的变量（参数）
        ret = num1 + num2
        print(ret)
    return func_inner # 返回的是内部函数，不是内部函数的执行

# 此时 num1=10就相当于被保存下来了
# todo f就是内部函数定义，num1=10被保存到f这个函数中了！
# todo f就是闭包（被返回的内部函数）！
# todo f这个闭包函数 把外部函数执行时产生的变量保存下来了！
f = func_out(num1=10)
f(1) # 怎么调用f这个函数，num1=10都生效、都存在！
f(1)


print('*'*10, 'nonlocal')

def func_out(b):
    a = b
    def func_inner():
        # nonlocal 不是全局的、不是本地的，所以只能是外部函数的
        nonlocal a # 声明我要使用 外部函数的变量 a
        a = a + 1 # todo 改变了外部函数的变量a的值
        print(a)
    return func_inner # 返回的是内部函数，不是内部函数的执行

# f是内部函数、闭包：保存了外部函数的变量a=100
f = func_out(b=100)
f() # 每次调用，都改变了外部变量a的值，且保存了改变值之后的外部变量a
f()

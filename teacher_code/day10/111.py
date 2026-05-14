def outer(x):
    # 外部函数定义了变量 x
    def inner(y):
        # 内部函数引用了外部的 x
        # 此时，inner 就形成了一个闭包
        return x + y
    return inner  # 把内部函数定义“打包”着送出去

# 制造一个闭包实例，它记住了 x=10
closure = outer(x=10) # 封闭包裹了变量x=10

# 哪怕在别的地方调用，依然记得 x=10
print(closure(5))  # 输出 15
print(closure(20)) # 输出 30
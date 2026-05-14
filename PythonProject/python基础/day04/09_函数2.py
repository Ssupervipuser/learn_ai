
def func1():
    print('函数1开始') # 效果2
    print('函数1结束') # 效果3

def func2():
    print('函数2开始') # 效果1
    # todo func2被调用执行时，func1函数才会被调用执行
    func1() # 调用执行 func1() 这个函数
    print('函数2结束') # 效果4

# 这里才开始真正的执行函数
func2() # 调用执行 func2() 这个函数

print('*'*5)

def func3():
    print(1)
    print(2)

def func4():
    print(3)
    func3()
    print(4)

def func5():
    print(5)
    func4()
    print(6)

func5()




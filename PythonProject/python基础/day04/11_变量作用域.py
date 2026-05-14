a = [1,2,3] # 全局变量
for i in a:
    # i 是全局变量！
    pass
# todo 某个变量出现之后，后续代码都能够使用 —— 全局变量

def func1(num):
    my_str = '111' # 局部变量 func1自己的变量
    print(num) # num形式参数 是func1自己的变量、局部变量
    print(my_str)

def func2(num):
    print(num) # num形式参数 是func2自己的变量、局部变量

func1(i)
func2(i)

print('*'*5)

num = 0 # 全局变量
def func3():
    num = 10 # 和全局变量同名的局部变量
    print('func3:', num)

func3()
print(num)

print('*'*5)

num2 = 0 # 全局变量
def func3():
    # todo global 变量名 ==>专门声明该变量是全局变量
    # todo global仅做声明，其他与我无关，不管变量的定义、创建
    global num2 # 声明，今后本函数中的num变量是全局变量了
    num2 = 10 # 修改全局变量num的值
    print(num2) # 此时num==0
    print('func3:', num2)

func3()
print(num2)

"""在函数中使用全局变量：
先函数外定义全局变量
再函数中global声明使用的是全局变量
最后在函数中使用全局变量
**注意：在函数中，声明全局变量前，不能出现全局变量同名的变量
"""

# for循环0-9，用函数实现判断条件，只打印输出偶数
def fun4(i):
    return True if i % 2 == 0 else False
# range(10) == <range(0,1,2,3,4,5,6,7,8,9)>
for i in range(10):
    if fun4(i):
        print(i)


import os

try: # 捕获异常
    print( 5 / 0 )
except: # try里边的代码出异常，就执行except中的代码
    print('出现异常了！')

# print( 5 / 0 ) # 异常错误类型：ZeroDivisionError

try: # 捕获异常
    print( 5 / 0 )
# except标记的错误类型符合的话，才执行except里代码
# except标记的错误类型不符合的话，依旧报错！
# except标记多个错误类型，用元组包裹多个错误类型
except (FileExistsError, ZeroDivisionError):
    print('出现异常了！')

try:  # 捕获异常
    print(5 / 0)
# todo 通过 except 异常类型 as 异常信息变量名（自定义的） ==>  就可以打印异常信息变量名
except ZeroDivisionError as eeeeee:
    print(ZeroDivisionError)
    print('出现异常了！')
    # 这个e 就是错误提示信息
    print(eeeeee) # division by zero

print('*'*10)
try: # 捕获异常
    # todo 第一个异常出现，后边代码就不执行了！
    os.mkdir('../day07')
    print(5 / 0)
# Exception是除了语法错误以外的其他所有错误、异常的父类（都包含了）
except Exception as e:
    print(e)
    print('出现异常了！')
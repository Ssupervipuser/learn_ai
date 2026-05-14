import traceback # 导包

try:
    print('语法错误是 syntax error')
    print('异常错误是 exception error')
    print('a'+11)
    print(22222)
    print('a'+11)

except Exception as e:
    # 仅输出异常提示信息
    print(e)
    print('*')
    # traceback.format_exc() 完整的异常堆栈信息（报错的位置）
    # traceback.format_exc() 只能放在 except中
    print(traceback.format_exc()) # 能够输出完整的异常信息！包括异常类型、提示、报错的位置
    print('*')
else: # except不执行，else才执行
    print('如果没有发生异常就执行这里')
finally:
    print('无论怎样都会执行这里')
    print('过分使用try except，会导致找不到问题所在位置，慎重使用')
    # print(traceback.format_exc())


print('【异常传递】')
def foo():
    print('foo start')
    print(num) # todo 报错的源头
    print('foo end')
def bar():
    print('bar start')
    # 代码运行至此才会引发异常
    foo() # todo 报错发生的导火索
    print('bar end')


# todo 哪怕try捕捉的异常没有处理，程序最终因为try代码中出的错误导致 code 1 终止运行
# todo 和try一起的finally也会执行！
try:
    bar()
finally:
    print('程序报错，我也执行！')
    print(traceback.format_exc())
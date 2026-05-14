# import traceback
# try:
#     print('语法错误是 sytanx error')
#     print('异常错误是exception error')
#     print('a'+11)
#     print(222)
#     print('a'+11)
# except Exception as e:
#     #仅输入异常提示信息
#     print(e)
#     #traceback.format_exc()完整地异常堆栈信息
#     # print(traceback.format_exc())
# else:
#     print('如果没有发生异常就执行这里')
# finally:
#     print('无论怎样都会执行这里')
#
# #和循环判断with open一样，try.except也可以嵌套，他们可以互相嵌套
# try:
#     try:
#         print(5/0)
#         #只补做专项异常
#     except:
#         print(traceback.format_exc())
# except:
#     print(traceback.format_exc())
#
# print('异常传递')
#
# def foo():
#     print('foo start')
#     print(num)#todo 报错的源头
#     print('foo end')
# def bar():
#     print('bar start')
#     #代码运行至此才会引发异常
#     foo()   #todo 报错发生的导火索
#     print('bar end')
# try:
#     bar()
# finally:print(traceback.format_exc())



from os import listdir
ret=listdir()
print(ret)

import os
ret=os.listdir()
print(ret)

import os as winos

ret=winos.listdir()
print(ret)


from os import listdir as win_listdir
ret=win_listdir()
print(ret)
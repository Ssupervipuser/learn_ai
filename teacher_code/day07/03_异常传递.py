
try:
    f = open('yyy.txt', 'w')
    # try异常处理可以嵌套
    try:
        ret = f.read()
        print(ret)
    except ZeroDivisionError: # 异常的类型不对，这个excpet不处理！
        print('这里不会被执行')
    # finally 异常出现了，finally中的代码都会执行
    finally: # 这里一定会执行！
        f.close()
        print('关闭文件')
# try嵌套的里边的try如果没有处理异常的话，就把异常向外传递
# 外层的try去捕捉、外层except再去处理
except Exception as e:
    print('外层：', e)

# print('*'*10)
# def func1():
#     print('func1开始')
#     print(num) # 出现异常错误！
#     print('func1结束')
#
# def func2():
#     print('func2开始')
#     func1() # 调用其他函数
#     print('func2结束')
#
# func2()
""" 
1. 最上边的错误位置是最外层的错误
2. 最下边的错误位置是错误的根源
3. 中间是错误传递的过程，本质是代码引用的过程

Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\1.python基础\code\day07\03_异常传递.py", line 30, in <module>
    func2()
  File "D:\BaiduNetdiskDownload\1.python基础\code\day07\03_异常传递.py", line 27, in func2
    func1() # 调用其他函数
    ^^^^^^^
  File "D:\BaiduNetdiskDownload\1.python基础\code\day07\03_异常传递.py", line 22, in func1
    print(num)
          ^^^
NameError: name 'num' is not defined. Did you mean: 'sum'?

"""
















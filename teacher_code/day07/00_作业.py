
# todo 作业 1. 异常
# traceback.format_exc() # 完整的异常堆栈信息
import traceback

try:
    print('语法错误是 sytanx error')
    print('异常错误是 exception error')
    print('a'+11)
    print(22222)
    print('a'+11)
except Exception as e:
    # 仅输出异常提示信息
    print(e)
    # traceback.format_exc() 完整的异常堆栈信息
    print(traceback.format_exc())
else:
    print('如果没有发生异常就执行这里')
finally:
    print('无论怎样都会执行这里')
    print('过分使用try except，会导致找不到问题所在位置，慎重使用')

try:
    try:
        print(5/0)
    except ZeroDivisionError:
        print(traceback.format_exc())
except:
    print(traceback.format_exc())

print('【异常传递】')
def foo():
    print('foo start')
    # print(num) # todo 打开这里注释会产生异常
    print('foo end')
def bar():
    print('bar start')
    foo()
    print('bar end')
# todo 为啥产生异常？如何修改代码解决异常让程序继续执行？
try:
    bar()
finally:
    print(traceback.format_exc())


# todo 作业2. 串讲笔记课件 【9.模块和包】 中的内容过一遍
# 2.0 注意命名要合规！
# 2.1 自定义2个模块，一个模块引用另外一个模块
# 2.2 自定义1个包，一个py文件中引用自定义的包
# 2.3 在自定义的、被引用的模块中，定义白名单，定义几个变量，白名单中添加1个变量名，运行程序入口的py文件 看效果
# 2.4 自定义包中 要求同上；友情提示：sys.path.append('自定义包的所在路径')


# todo 作业3. 学生管理系统： 照着写！写注释！别自个写！
# 写不完没关系，留到放假再写！
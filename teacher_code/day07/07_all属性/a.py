
# todo 定义本模块的白名单
# 列表中有名字的变量或函数
# 在其他文件导入模块时，是：from a import *，能够被调用
# 列表中没有的，就不能被调用，且报错
__all__ = ['sum', 'foo']
"""
在别的文件中 from a import *
* ==> __all__
"""


sum = 10

def foo(a, b):
    return a+b

def bar(a, b):
    return a-b
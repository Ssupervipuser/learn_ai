
# 当别的文件调用此文件时，导包形式是 from toolsbar import *
# all白名单才生效，列表中有名字的函数、变量、类，才能够被使用
__all__ = ['func1', 'toolsbar_v3']

def func1():
    func2()
    return '这是toolsbar的func1函数'

def func2():
    return '这是toolsbar的func2函数'

toolsbar_v4 = 200
toolsbar_v3 = 100 + toolsbar_v4



import os

print(os.__name__) #内置属性模块名字

print(os.listdir.__name__) #内置属性函数名字

print(__name__)    #当前正在运行的模块名字，永远是__main__

#引用 了b文件，b文件发生了运行
import b
print(b.__name__)

if __name__ == '__main__':
    print('aaaa')
    print(__name__)


__all__ =['foo','my_int']

my_int=666

def foo():
    return my_int

def bar():
    return 777












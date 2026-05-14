
print(__name__)
# 直接运行a.py时，输出 '__main__'
# 运行b.py时，输出 a

print(111)

def foo(a, b):
    print(a+b)
    return a+b

if __name__ == '__main__':
    print(__name__)
    print('a.py')
    foo(1, 2) # 测试本模块.py文件中代码的功能

# todo python导入包模块的顺序：先内置、再三方、最后自己写的、系统路径
# import abc  # 这里的问题：python本身自己有一个abc这样模块
import a
# todo 运行b.py时 import a 相当于 把a.py执行了一遍
# a.py中 print(__name__) 输出的是 模块名 a

print(__name__) # '__main__'
"""
__name__ 是python内置变量，是模块的名字
在本模块中，值是 '__main__'
如果是引用了别的模块，那个被引用的模块的__name__ 就是模块名
"""

# todo 一般写在.py文件中最后，作用是：
# todo 1.测试当前的.py文件中的功能
# todo 2.作为程序入口
if __name__ == '__main__': # 程序入口
    # 如果该判断成立，说明：
    # 运行的就是当前这个文件、当前这个模块
    print(__name__)
    print('b.py')

    a.foo(1, 2)

# todo 查看当前能够导包、模块的路径
import sys
print(sys.path)


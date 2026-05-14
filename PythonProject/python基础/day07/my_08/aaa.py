
# todo 1. 如何添加自定义的包

import sys
print(sys.path) # 查看python能够导包的路径，包都什么位置

# 自定义的包的路径
my_moudle_path = 'D:/BaiduNetdiskDownload/1.python基础/code'
sys.path.append(my_moudle_path) # 添加定义包的所在目录的路径
print(sys.path)

# 2. 导入自己实现的包或模块
from my_081 import *
# 3. 导入的自定义包一定在程序入口文件的同级
# 4. 导入自定义包的时候，不要以pycharm为准，以cmd终端运行为准！


"""python的虚拟环境 是python代码运行的环境依赖
作用是做环境隔离，最好一个项目一个python环境
虚拟环境的本质是 在一个指定的位置 复制过去一个python解释器 用这个解释器 运行相应的代码
"""




import os
import sys
import asyncio

print(sys.path) # python运行时导包会找的路径，以cmd终端为准！
# sys.path.append('自定义包的所在路径')


# __name__ 叫做内置变量，大家都有
print(os.__name__)
print(os.listdir.__name__)
print(asyncio.__name__)


def 入口程序函数():
    pass

# 所有直接被运行的py文件的 name 属性值 都是 '__main__'
# 被调用的模块、包的 name 属性值 都是模块、包的名字
# 1. 区分当前谁是直接被运行的py文件，谁是被调用的包、模块
# 2. 被调用的py文件中，可以在if __name__ == '__main__':后边写测试功能的代码
# 3. 被直接运行的py文件中，可以在if __name__ == '__main__':后边写启动程序的代码
if __name__ == '__main__':
    print('当前文件被直接运行的时候，这里才执行')
    入口程序函数()
from loguru import logger as log

# 获取当前操作系统默认的编码方式
import sys
print(sys.getdefaultencoding())

# w 是覆盖写  r 是读 a 是追加写
with open('1.txt', 'w', encoding='utf-8') as f:
    content = '内容'
    f.write(content)
    log.info('记录当前写文件的内容: {}'.format(content))

# 备份文件
with open('1.txt', 'r', encoding='utf8') as fr:
    content_str = fr.read()

# 完整的路径包括文件名字！
# new_filepath = '../备份文件夹/1[备份].txt'
# with open(new_filepath, 'w', encoding='utf8') as fw:
#     fw.write(content_str)

# todo 相对路径绝对路径
# 1.txt == 》 ./1.txt


# todo 异常处理
# 语法错误Syntax 和 其他错误都叫异常Exception
import traceback

# 自定义日志信息
log.debug('debug级别调试消息')
log.success('成功调用')
log.info('普通消息') # 常用
log.warning('警告消息')
log.error('错误消息')
log.critical('严重错误消息')

try:
    print( 5 / 0 )
    # print(1111)
    log.info(1111)
except Exception as e:
    print(e) # 优先的错误提示信息
    print(traceback.format_exc()) # 打印完整的异常信息
    log.exception('异常') # 日志记录完整的异常信息
else: # except执行了 else这里就不执行
    log.info('except不执行、没异常，就执行else')
finally:
    log.warning('永远都会执行finally中的代码')

try:
    try:
        print('1'+1)
    except ZeroDivisionError:
        log.exception('ZeroDivisionError')
except Exception:
    log.exception('被传递出来的异常')


log.info('*'*10)

"""
包：包含__init__.py文件的文件夹
模块：命名规范的一个py文件

包、模块的作用：
1. 在逻辑上去分割代码，让代码可读性更好
2. 方便多人分工合作

包：工具合集
模块：一类、一组工具
模块中的内容：具体的工具

平时沟通时，包和模块不做区分
"""
# todo 导包的方法
import os, asyncio # 直接导入包或模块
import asyncio.locks as lock # 直接导入包.模块
from asyncio import locks # 基于包导入模块
from asyncio.locks import Event as ev # 基于包.模块导入内容（函数、变量、类）

# __name__ 内置属性：谁都有！就是自己的名字！
log.info(asyncio.__name__)
log.info(os.__name__)
log.info(ev.__name__)
# 模块的__name__=='__main__'的时候：
if __name__ == '__main__':
    log.info('说明当前的这个模块这个py文件是直接被运行的')
    """ 当多个py文件共同完成一个程序任务时，
    每个不直接被运行的py文件自己可以在这个位置，做功能测试
    """

# todo __all__属性：需要自定义、能够被使用的白名单列表
from toolsbar import *
func1()
# func2() # 不能用

# todo python解释器搜索包、模块的路径
import sys
log.info(sys.path) # python解释器就从这里去找包、模块
# 添加自定义包所在的目录的绝对路径，才能正确的导入自定义的包
sys.path.append('D:/BaiduNetdiskDownload/1.python基础/code')
log.info(sys.path)

import my_081 # 包被调用时，__init__.py自动执行
import my_081.abcdef # 模块被调用时，该py文件自动被执行
import os # 模块被调用时，os.py自动被执行

# todo 三方包：需要pip install安装的就是三方包
# 内置包 自定义包 三方包
# python解释器完整路径 -m pip install 三方包的名字 -i https://pypi.tuna.tsinghua.edu.cn/simple/
# D:\ProgramData\anaconda3\python.exe -m pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
# D:\ProgramData\anaconda3\python.exe -m pip uninstall requests

import requests



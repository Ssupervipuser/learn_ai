"""
python的包就是一个文件夹、包含__init__.py文件
说 导包，但实际导入的是一个模块 ———— 这么说没错
python 包和模块是一个类型

"""
# import (包名.)模块名
import os

print(os) # <module 'os' (frozen)>
print(type(os))


import asyncio # 只运行 asyncio包中的__init__.py文件
import asyncio.futures
print(asyncio) # <module 'asyncio...>
print(type(asyncio))

# from 包名 import 模块名
from asyncio import futures

# from 包名.模块名 import 要用的类、函数、变量
from asyncio.futures import *

import random, json

import requests # 不是python解释器自带的 需要额外安装的 都是三方包

# todo 三方包的安装
""" 通过命令的方式
哪个python解释器去安装的第三方包——要确定！
D:/ProgramData/anaconda3/python.exe -m pip install requests
D:/ProgramData/anaconda3/python.exe -m pip unstall requests
D:/BaiduNetdiskDownload/1.python基础/code/venv/Scripts/python.exe -m pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
D:/BaiduNetdiskDownload/1.python基础/code/venv/Scripts/python.exe -m pip unstall requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
"""


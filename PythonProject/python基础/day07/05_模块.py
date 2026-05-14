import os # 导入的是整个os.py

# 在os.py文件中，导入了nt.py中的一切，nt.py中有一个getcwd的函数
os.getcwd()

# 表示导入copy中的所有内容
from copy import *

# as dp 表示 给deepcopy改名，叫做dp
from copy import deepcopy as dp

print(__name__) # __main__

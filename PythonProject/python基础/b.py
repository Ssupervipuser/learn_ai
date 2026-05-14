# print(__name__)
#
#
# import traceback
# from a import *
#
# try:
#     print(my_int)
#     print(foo())
#     print(bar())
# except:
#     print(traceback.format_exc())
#
# from a import bar
# print(bar())

import sys
print(sys.path)

sys.path.append('D:\my_station\code\PythonProject\python基础\自定义包')





if __name__=="__main__":
    #如果被其他py文件引用，这里将不会执行
    #因为被引用时，b.py的__name__是b，而不是__main__
    #只有b.py作为主文件运行时，b的__name__才是__main__
    print('bbb')
    print(__name__)



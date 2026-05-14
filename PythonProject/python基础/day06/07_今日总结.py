# 查看当前操作系统默认编码格式
import os
import sys
print(sys.getdefaultencoding()) # utf8
my_sys_default_encoding = sys.getdefaultencoding()

print('写文件')
with open('./111.txt', mode='w', encoding='utf-8') as fw:
    fw.write('职业法师刘海柱\n')
    fw.write('雷电法王杨永信\n')
print('a模式是追加写')
with open('./111.txt', mode='a', encoding='utf-8') as fw:
    fw.write('我没开挂卢本伟\n')
    fw.write('泪含珍珠周淑怡')
# print('a+模式是又读又写')
# with open('./111.txt', mode='a+', encoding='utf-8') as fw:
#     fw.write('我没开挂卢本伟\n')
#     fw.write('泪含珍珠周淑怡')
#     print(fw.read())

print('读文件')
with open('./111.txt', 'r', encoding='utf-8') as fr:
    print(fr.read()) # 读全部
with open('./111.txt', 'r', encoding='utf-8') as fr:
    print(fr.read(5)) # 读5个字符
with open('./111.txt', 'r', encoding='utf-8') as fr:
    print(fr.readline()) # 读一行
with open('./111.txt', 'r', encoding='utf-8') as fr:
    print(fr.readlines()) # 读所有行
with open('./111.txt', 'r', encoding='utf-8') as fr:
    print(fr.readline(4)) # 读一行中前4个字符

print('逐行读')
with open('./111.txt', 'r', encoding='utf-8') as fr:
    while True:
        res = fr.readline() # 读一行
        print(res, end='')
        if res == '':
            break

# print('bytes模式：wb rb ab')
# with open('./111.txt', 'rb') as fr:
#     print(fr.read())

# todo 一个文件在写的时候如果是用gbk编码方式组织的文本内容
# todo 读的时候也得用 gbk； utf8也是如此


""" todo 相对路径和绝对路径
.  # 当前路径
.. # 上一级
./c.txt # 当前路径下的c.txt
../../a/b/c.txt
# 以当前路径为基准，上一级的上一级下边的a文件夹中的b文件夹中的c.txt文件
# os.getcwd() 返回当前位置的绝对路径

绝对路径： 以/或C:盘符开头的都是绝对路径
"""

# todo os模块中功能函数
os.listdir() # 返回当前路径下有哪些文件和文件夹
# os.rename('旧完整路径', '新完整路径') # 给文件改名
os.path.exists('文件或文件夹的完整路径') # 判断是否存在
os.path.isfile('完整路径') # 判断是否为文件，不存在的路径也是False
os.remove('完整路径') # 删除文件
os.mkdir('完整路径') # 创建文件夹
os.rmdir('完整路径') # 删除文件夹

# 查看当前的工作路径、当前的位置
os.getcwd()
# 切换当前的工作路径、当前位置
os.chdir('目标位置的完整路径')
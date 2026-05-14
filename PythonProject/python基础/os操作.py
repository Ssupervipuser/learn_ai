import os

#创建文件
# with open('1.txt','w',encoding='utf-8') as f:
#     f.write('代排了老铁')
#创建文件夹
# os.mkdir('./haha')
# print(os.listdir('./haha'))

#文件/文件夹重命名
# os.rename('.haha','haha')
# os.rename('1.txt','2.txt')

#查看指定路径下有哪些文件和文件夹
print(os.listdir())
#删除文件
# os.remove('2.txt')
#删除文件夹
# os.rmdir('haha')
#查看当前工作目录位置

# print(os.getcwd())

#改变工作目录位置
# os.chdir('../')
# print(os.listdir())

#判断路径（文件/文件夹）是否存在
print(os.path.exists('haha'))
print(os.path.exists('../python进阶/多态.py'))
#判断文件（不是文件夹）是否存在
print(os.path.isfile('../python进阶/多态.py'))
print(os.path.isdir('../.idea'))

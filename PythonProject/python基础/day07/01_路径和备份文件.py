import os
"""
1. 写对：位置 = 路径 = 名字 = 完整的名字 = 完整的路径 = 绝对路径 = 相对路径
2. 目标文件夹、目标路径的上一级文件夹必须存在
"""

print(os.getcwd()) # 当前位置
# D:\BaiduNetdiskDownload\1.python基础\code\day07

# 要备份的文件的位置、路径、名字
# 绝对路径：D:\BaiduNetdiskDownload\1.python基础\code\day07\要备份的文件.py
# 相对路径：./要备份的文件.py

# 目标位置、路径、名字
# 绝对路径：D:\BaiduNetdiskDownload\1.python基础\code\备份文件夹\要备份的文件[备份].py
# 相对路径：../备份文件夹/要备份的文件[备份].py


# 1. 先创建备份文件所在的文件夹、路径
dirpath = '../备份文件夹'
# if not os.path.exists(dirpath): # 不存在才创建
#     os.mkdir(dirpath)
try:
    os.mkdir(dirpath)
except:
    pass

# 2. 读取要备份文件的内容
old_filepath = './要备份的文件.py' # 要备份的文件的完整路径、名字
with open(old_filepath, 'r') as fr:
    content_str = fr.read()

new_filepath = '../备份文件夹/要备份的文件[备份].py' # 目标文件的完整路径、名字
# 3. 写入备份文件中
with open(new_filepath, 'w') as fw:
    fw.write(content_str)


# todo 下边是拼接完整路径实现方式，下边的代码实际就是29行代码的具体实现方法
old_filepath = './要备份的文件.py'
目标是 = '../备份文件夹/要备份的文件[备份].py'

原文件路径字符串倒排 = old_filepath[::-1]
print(原文件路径字符串倒排) # yp.件文的份备要/.
文件扩展名前边的点的倒排后的下标 =  原文件路径字符串倒排.find('.')
print(文件扩展名前边的点的倒排后的下标) # 下标是2
# 以当前old_filepath为例：正排的时候，关键的点下标是-3
# 怎么把2变成-3呢 ==> -(2+1)
原文件路径中最后的那个点的下标 = -(文件扩展名前边的点的倒排后的下标+1)
print(原文件路径中最后的那个点的下标) # -3
# 分割原文件路径、名字
文件名前半部分不要点和扩展名_不完整还缺最前边的路径 = old_filepath[1:原文件路径中最后的那个点的下标]
print(文件名前半部分不要点和扩展名_不完整还缺最前边的路径) # /要备份的文件
点和文件扩展名 = old_filepath[原文件路径中最后的那个点的下标:]
print(点和文件扩展名)

dirpath = '../备份文件夹'
# 拼接完整的路径、名字
目标完整路径 = dirpath + 文件名前半部分不要点和扩展名_不完整还缺最前边的路径 + '[备份]' + 点和文件扩展名
print(目标完整路径) # ../备份文件夹/要备份的文件[备份].py


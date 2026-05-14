
# 分别用utf8\gbk编码方式 写入文本文件内容
# w模式是覆盖写
with open('utf8-file.txt', 'w', encoding='utf8') as f:
    f.write('utf8中文')
with open('gbk-file.txt', 'w', encoding='gbk') as f:
    f.write('gbk')


# 分别用utf8\gbk编码方式 读取文本文件内容
with open('utf8-file.txt', 'r', encoding='utf8') as f:
    print(f.read())
with open('gbk-file.txt', 'r', encoding='gbk') as f:
    print(f.read())
"""
# 打开一个文件，路径是 filename, r/w是读或写
# encoding='utf8' 对文件的内容到底是以什么样的编码方式去读去写
with open(filename, 'r/w', encoding='utf8') as f:
    f.write('你要写入文件的内容') # w模式
    f.read() # 全读，返回字符串
    f.read(5) # 从光标开始读取5个字符，返回字符串
    f.readline() # 读取一行，行以\n结束，返回字符串
    f.readlines() # 读取全部行，每行作为元素构成列表返回
    pass
print()
"""

# todo 相对路径和绝对路径
# 用相对路径去打开test2.txt文件，写入文本数据
filepath = './code2/test2.txt' # 相对路径
filepath = 'code2/test2.txt' # 相对路径
with open(filepath, 'w', encoding='utf8') as f:
    f.write('相对路径：相对的是当前工作的路径\n绝对路径：从磁盘根节点开始的完整路径')

# 用绝对路径去打开test2.txt文件，读取文本数据
filepath = 'D:/BaiduNetdiskDownload/1.python基础/code/day06/code2/test2.txt'
with open(filepath, 'r', encoding='utf8') as f:
    print(f.read())
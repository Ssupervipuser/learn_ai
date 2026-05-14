import os # 导包 python内置的os模块

# 查看【当前路径】下的所有文件、文件夹，返回列表
# 这里的【当前路径】是指代码运行的工作目录
print(os.listdir('./'))
# 查看【当前路径】
print(os.getcwd())

# 给文件改名
# if 要改的文件存在：
if os.path.exists('1.txt'):
    ret = os.rename('1.txt', 'hahaha.txt')
    print(ret)
else:
    print('不存在，所以不执行给文件改名')

# 判断路径(文件、文件夹)是否存在
print(os.path.exists('1.txt'))
filepath = 'D:/BaiduNetdiskDownload/1.python基础/视频/day07'
print(os.path.exists(filepath))
# 判断这个文件存在不存在，判断是否是文件
print(os.path.isfile('2.txt'))
# code1存在，但是个文件夹，所以返回False
print(os.path.isfile('code1'))

# 删除指定的文件
if os.path.exists('hahaha.txt'):
    os.remove('hahaha.txt')
    print(os.listdir('./'))
else:
    print('不存在，所以不执行删除文件')

# 创建文件夹
if os.path.exists('./code3'):
    # print('已存在所以不创建')
    pass
else:
    os.mkdir('./code3')
if not os.path.exists('./code3'):
    os.mkdir('./code3')
else:
    print('已存在所以不创建')
    pass


# 查看【当前路径】
print(os.getcwd())

# 改变了工作路径
os.chdir('../')
# 查看工作路径
print(os.getcwd())
# 再创建就不报错了
if not os.path.exists('./code3'):
    os.mkdir('./code3')



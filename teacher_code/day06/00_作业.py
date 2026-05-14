

# todo 1. filter函数

lst = [i for i in range(1,11)]
lst = [1, 2, 3, 4, 5,
       6, 7, 8, 9, 10]

def func(i):
    """
    判断函数
    :param i: 传入的一个数字
    :return: True 或 False
    """
    return i % 2 == 1

# todo filter函数：对传入的第2个参数（列表），基于第一个参数（函数名）进行过滤
# todo 第一个参数是函数名，该函数返回True或False
# todo True时传入的那一个遍历出来的元素保留
res = filter(func, lst)
print(list(res))

# filter函数中第一个参数可以用lambda
res = list(filter(lambda i: i%2==1, lst))
print(res)


# todo 2. map函数，需求：把负数全变成正数，返回新列表
lst2 = [-5, 3, -7, -99, 8, -9]
# 1. 定义函数，将传入的每个元素判断正负，正数不变、负数改正数
def func(i):
    # if i > 0:
    #     return i
    # else:
    #     return -i
    return i if i>0 else -i
func = lambda i: i if i>0 else -i
# 2. map函数+list函数，返回新的全是正数的列表
res = list(map(func, lst2))
print(res)


# todo 3. reduce函数
# 需求：计算1-100的和，reduce函数实现
from functools import reduce
def func(x, y):
    # 计算第一个元素 + 第二个元素，返回计算结果
    # 上一次计算结果 + 第三个元素，返回计算结果
    # ...
    # 上一次计算结果 + 最后一个元素，返回计算结果
    return x + y
func = lambda x, y: x+y
lst = list(range(1, 101))
# 1-100的和 = reduce(函数, [1-100])
"""
将lst中前2个元素，传入func函数，该函数得到一个结果
这个结果、第3个元素，再传入func函数，得到一个新的结果
新结果、第4个元素，再传入。。。直到最后一个元素
"""
res = reduce(func, lst)
print(res)


# todo 4. round函数练习
# 需求：把列表中所有数字，全部按四舍五入变成3位小数
lst = [0.34567, 1.6568596859, 0.21782121]

lst2 = [round(i, 3) for i in lst]
print(lst2)

lst2 = list(map(lambda i:round(i, 3), lst))
print(lst2)


# todo 5. 需求：写个函数 使用reduce和lmabda实现阶乘
from functools import reduce
# 阶乘：5*4*3*2*1  3*2*1
def func(num):
    # 定义列表
    # ret = list(range(num,0,-1))
    # print(ret)
    # lambda 实现对传入的每一个元素进行乘法、返回结果
    res = reduce(lambda x, y: x * y, list(range(num,0,-1)))
    return res
print(func(num=5), '<------计算阶乘')


# todo 6. 读文件并输出，需求：用行读取的方式读取 00_作业.py 文件，打印每一行，直到读取打印完毕
with open('00_作业.py', 'r', encoding='utf8') as f:
    content_list = f.readlines()
    for content in content_list:
        print(content, end='')


# todo 7. 找一个文件，给他备份
# 1. 指定文件、获取文件的完整路径
filepath = './code2/test2.txt' # 要备份的文件的路径
# 2. 根据要备份的文件 定义新文件的名字： xxx[备份].xxx
# 2.1.找最后一个点的下标
xiabiao = - (filepath[::-1].find('.') + 1)
print(xiabiao)
# 2.2.切片、拼接
new_fp = filepath[:-4] + '[备份]' + filepath[-4:]
# ./code2/test2[备份].txt
print(new_fp)
# new_fp = './code2/test2[备份].txt'
# 3. 根据新备份文件的完整路径创建新文件，w写方式
with open(new_fp, 'w', encoding='utf8') as fw:
    # 4. 读取要备份的旧文件中的文本内容
    with open(filepath, 'r', encoding='utf8') as fr:
        content_str = fr.read()
    # 5. 旧文件文本内容写入新备份文件
    fw.write(content_str)


# todo 8. 串讲笔记课件 7.操作文件

# todo 【可以不做！】
# todo 9. 需求：备份当前路径下所有的文件
# todo 保存到当前文件夹同级的新文件夹中
# ps: day06下的所有文件，复制保存到 day06同级的 day06备份 文件夹中
import os
# 1. 找出所有文件

# 1.1 获取当前工作的路径
dangqian_path = os.getcwd()
print(dangqian_path)

# 1.2 获取指定路径下所有的文件和文件夹的名字
file_dir_list = os.listdir(dangqian_path)
print(file_dir_list)

# 1.3 判断是不是文件，把文件名保存一个新列表中
file_list = [name for name in file_dir_list
              if os.path.isfile(name)]
print(file_list)

# 2. 创建保存备份文件的文件夹
new_dir_path = '../day06备份' # 新文件夹
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
print(os.listdir('../'))

# 3. 定义备份文件的功能函数
def read_old_write_new(new_fp, old_fp):
    """【注意】 路径别错了！
    把旧文件的内容写入新文件
    :param new_fp: 新文件的完整路径
    :param old_fp: 旧文件的完整路径
    :return: None
    """
    # 3. 根据新备份文件的完整路径创建新文件，w写方式
    with open(new_fp, 'w', encoding='utf8') as fw:
        # 4. 读取要备份的旧文件中的文本内容
        with open(old_fp, 'r', encoding='utf8') as fr:
            content_str = fr.read()
        # 5. 旧文件文本内容写入新备份文件
        fw.write(content_str)

# 4. 每个文件都进行读取，在新的路径中写入同名的文件中
for old_file in file_list:
    # new_dir_path = '../day06备份/xxx.xxx'
    new_fp = new_dir_path + '/' + old_file
    print(f'正在备份{old_file}到{new_fp}中...耐心等待')
    read_old_write_new(new_fp, old_file)
    print(f'正在备份{old_file}到{new_fp}完成')



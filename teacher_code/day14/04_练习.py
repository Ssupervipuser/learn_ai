import math

def dataset_loader(bath_size):
    # todo bath_size参数：生成器每次返回数据的数量
    # 1. 读取文件
    file_path_name = './歌词.txt'
    with open(file_path_name, 'r', encoding='utf8') as f:
        lines_list = f.readlines()
    # 2. 统计有多少行
    nums = len(lines_list) # 5行歌词
    # print(nums, type(nums))
    # 3. nums/bath_size == > 5/2=2.5
    # math.ceil(2.5) ==> 3 向上（往大数字）取整
    # math.ceil(-2.0001) ==> -2 向上（往大数字）取整
    batch_number = math.ceil(nums/bath_size) # 3
    # print(batch_number)
    # print(type(batch_number))
    # 4. range(3) ==> 0、1、2
    for idx in range(batch_number):
        # print(idx * bath_size) # 左边的下标 0 2 4
        # print(idx * bath_size + bath_size) # 右边的下标 2 4 6
        # lines_list[下标:下标] 范围：
        #  lines_list[0:2] 歌词.txt的第1、2行
        #  lines_list[2:4] 歌词.txt的第3、4行
        #  lines_list[4:6] 歌词.txt的第5、6行
        yield lines_list[idx * bath_size : idx * bath_size + bath_size]
        # yield就说明这是个生成器函数，返回生成器对象
# print(math.ceil(-2.0001))
# 调用生成器函数，返回生成器对象
# g = dataset_loader(bath_size=5)
# for lst in g:
#     print(lst)


import math

def dataset_loader(bath_size: int):
    # bath_size参数：每批要处理的文本的行数（一次训练bath_size行的数据）
    file_path_name = './歌词.txt'
    with open(file_path_name, 'r', encoding='utf8') as f:
        lines_list = f.readlines() # 读文件所有行
        # 返回 一行文本字符串构成一个元素 的 列表
    lines_count = len(lines_list) # 获取 文本的行数
    # 行数 除以 每批处理的行数 ，等于 多少批
    batch_number_float = lines_count / bath_size # 有可能是小数
    # 向上取整数 math.ceil(float)，得到最终批次
    batch_number_int = math.ceil(batch_number_float)
    # todo lines_count: 每批处理多少行文本数据
    # todo batch_number_int: 多少批 （总行数 除以 每批处理的行数）
    # todo bath_size：每批要处理的文本的行数（一次训练bath_size行的数据）
    for idx in range(batch_number_int): # 假设 batch_number_int==3，那么idx==0，1，2
        # 下标分析：第一次【0* ：bath_size】，第二次【bath_size：2*bath_size】，第三次【2*bath_size：3*bath_size】
        # yield lines_list[idx * bath_size: (idx+1) * bath_size]
        yield lines_list[idx * bath_size : idx * bath_size + bath_size]
        # todo yield让函数变成生成器函数：遍历一次返回一次

# g：生成器对象！
g = dataset_loader(bath_size=5)
for lst in g: # 遍历生成器对象！
    # lst：要处理的一批歌词文本str
    print(lst) # 模拟投喂给模型进行训练


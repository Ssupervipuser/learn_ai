# 1. 剪刀石头布

import random


def caiQuanGame(nums, is_player_bool=True):
    """猜拳函数：
        电脑随机出
        玩家自己出或随机出，基于is_player_bool是否为True
        电脑 - 玩家 的结果 有3种情况：
            0 平局
            -1 or 2 电脑胜
            1 or -2 玩家胜
    :param nums: 没用！只是告诉我们参数可以进来，也可以传出去
    :param is_player_bool: True，让玩家输入
                           False，玩家也随机出
    :return: result_str，平局 or 电脑胜 or 玩家胜
    """

    # 获取电脑的出拳，随机1-3
    computer_int = random.randint(1,3)

    # 玩家出拳
    # 如果is_player_bool是True
    if is_player_bool:
        # 玩家自己出拳
        player_str = input('\n 1：石头 \n 2：剪刀 \n 3：布 \n玩家请输入：')
        player_int = int(player_str)
    else: # 玩家也随机
        player_int = random.randint(1,3)

    # 相减
    ret =  computer_int - player_int

    # 根据相减的结果判断输赢
    if ret == 0:
        result_str = '平局！'
    else:
        # -1、2 电脑赢，其他情况是玩家赢
        result_str = '电脑胜利！' if ret == -1 or ret == 2 else '玩家胜利！'

    # 返回多个结果时，会被构造成一个元组
    return nums, result_str

# nums, is_player_bool=True
# ret = caiQuanGame(1, True)
# print(ret)


def main():
    """程序主逻辑：让游戏根据要求的次数进行循环
    :return: (游戏次数, 游戏结果)
    """
    nums = int(input('输入游戏次数：'))
    # 确定玩家是否需要随机出拳
    is_player = input('是否自动进行游戏？输入【是】或【否】：')
    # 把输入的是或否 转换成 True 或 False
    is_player_bool = True if is_player == '否' else False

    i = 1
    while 1:
        # 循环 nums 次，到次数了就退出循环
        if i > nums:
            break
        # 控制循环次数
        i += 1

        # 调用猜拳游戏函数，传入相应的参数
        ret = caiQuanGame(nums, is_player_bool)
        print(ret) # (1, '玩家胜利！') 元组

    print('游戏结束了')


# 运行游戏
# main()


# 2. 容器类型过一遍

# todo 列表 list [a]
lst = []
lst1 = [1]
lst = [1, 2, 3]
lst4 = lst1+lst
print(lst4) # [1, 1, 2, 3]

# list添加元素
lst.append(4) # 从右侧、队尾添加元素
print(lst)
# list删除元素
lst.remove(1)
print(lst)

del lst[0]
print(lst, '<==del根据下标删除list中元素的效果')

# 修改list中的元素的值
lst[-1] = 5 # 通过下标修改指定元素的值
print(lst)
# 根据下标查看list中指定的元素
ret = lst[1]  # 查看第2个元素，下标从0开始
print(ret, lst)
new_lst = lst[::-1] # 切片返回的是新的列表
print(new_lst, lst)
# 个数、最大最小值、求元素值的和
print(len(lst), max(lst), min(lst), sum(lst))
# list中元素根据值排序（前提是能够排序）
lst.sort() # 升序
lst.sort(reverse=True) # 降序
lst.sort(reverse=1) # 降序
# 判断元素是否在list中
if 2 in lst: print('存在')
if 2 not in lst: print('判断元素不在list中')
# list的遍历
for v in lst: # 遍历列表中每一个元素值
    print(v)
for i, v in enumerate(lst): # 遍历列表中每一个元素的下标和值
    print(i, v)
# 列表的推导式
new_lst = [v*2 for v in lst]
print(new_lst, lst, '<==查看列表推导式的效果')
# 通过列表推导式，把列表中元素的下标拿出来，组成一个新的列表
lst = ['刘海柱', '段誉', '西门长海', '公孙丽蓉']
i_lst = [i for i, _ in enumerate(lst)] # _ 表示 这个变量我不要了！
print(i_lst, '<==推导式效果')
# _ = 12345
# print(_)

# todo 切片
print(lst[::-1]) # 倒排
print(lst[:-1]) # 不要最后一3个元素
print(lst[2:0:-1]) # 从右往左，步长为1，从下标2到下标0，但不要最后的0

# todo 元组 tuple (a,) 不能增删改元组中的元素
tpl = ()
# tpl = (1) 错了
tpl = (1,)
# 列表、元组的互相转换
tpl = tuple(['刘海柱', '段誉', '西门长海', '公孙丽蓉'])
lst = list(tpl)
print(tpl)
# 元组通过下标查看指定的元素的值
print(tpl[-2])
print(tpl[::-1]) # 可以切片，返回的是新的元组
# 求元组中元素的个数、最大值、最小值、求和
tpl2 = (1, 2, 3)
print(len(tpl), max(tpl2), min(tpl2), sum(tpl2))
# 判断某个元素是否在元组中
if '段誉' in tpl: print('在')
if '钢铁侠' not in tpl: print('不在')
# 遍历元组
for v in tpl:
    print(v)
for i, v in enumerate(tpl):
    print(f'下标是{i}, 值是{v}')
# 元组推导式
new_tpl = tuple([i for i,_ in enumerate(tpl)])
print(new_tpl)

# todo 集合 set {a,b,c} 自带去重功能、没下标不能切片
st = set() # 空集合
# st = {} 错了！
# 元组添加元素
st.add(1)
st.add(2)
print(st)
# 元组删除元素
st.remove(1)
print(st)
# 从集合中取出一个元素，取出后集合中就没有这个元素了
v = st.pop()
print(v, st)
# 集合可以计算元素个数，最大值、最小值、元素值求和
st = {1,2,3}
print(len(st), max(st), min(st), sum(st))
# todo 虽然集合没有下标无序，也是能够遍历的
for v in st:
    print(v)
for 序号, v in enumerate(st):
    print(序号, v)
# 集合也可以写成推导式
lst.append('刘海柱')
print(lst)
st2 = {v for v in lst}
# 通过转成集合、做去重，再转回去
print(st2)
lst2 = list(st2)
print(lst2)
print(set(lst)) # 转成集合

# todo 列表、元组、集合 可以互相转换
# list(x)
# tuple(x)
# set(x)

# todo 字典 dict {k:v,...}
# 由key,value用冒号连接、成对出现，每个键值对之间用逗号分割
# 在一个字典中，key键不能重复
dt = {} # 空字典
dt = dict() # 空字典
my_dict = {'name': 'smart', 'age': 18, 'city': '上海'}
# 字典中增加kv键值对
my_dict['gender'] = '男'
print(my_dict)
# 通过key删除键值对
del my_dict['name']
print(my_dict, '<==删除kv的效果')
# 修改：通过对已经存在的key的值重新赋值
my_dict['gender'] = '女'
print(my_dict)
# 根据key查看值
print(my_dict['age'], my_dict.get('age'))
# 根据key取出值，取出之后字典中就没有这个键值对了
ret = my_dict.pop('city')
print(ret, my_dict)
# 除了len求字典中kv的个数，其他max、min、sum都是对key键进行操作
my_dict2 = {0:'a', 1:'b', 2:'c'}
print(len(my_dict2), max(my_dict2), min(my_dict2), sum(my_dict2))

# 判断 key 是否在字典中
if 'age' in my_dict.keys(): print('存在')
if 'age' not in my_dict: print('不存在')
# 判断 值 是否在字典中
if '女' in my_dict.values(): print('存在')
if '女' not in my_dict.values(): print('不存在')

# 遍历字典的key
for k in my_dict:
    print(k)
for k in my_dict.keys():
    print(k)
# 遍历字典的value
for v in my_dict.values():
    print(v)
# 遍历字典的 k 和 v
for k, v in my_dict.items():
    print(k, v)
# 遍历字典的 下标、key、value
for i, k in enumerate(my_dict):
    print(i, k) # 1 gender
for i, kv_tuple in enumerate(my_dict.items()):
    print(i, kv_tuple) # 1 ('gender', '女')
for i, (k, v) in enumerate(my_dict.items()):
    print(i, k, v) # 1 gender 女

# 字典的key或value转成其他类型
ks = list(my_dict.keys())
vs = list(my_dict.values())
print(ks, vs)
print(list(my_dict.items())) # [('age', 18), ('gender', '女')]

# 字典推导式错误方式：慎用、别用
print(my_dict)
new_dict = {k:v for v in vs for k in ks}
print(new_dict)
new_dict = {k:v for k in ks for v in vs}
print(new_dict)
# 相当于
new_dict = {}
for k in ks: # age,gender
    for v in vs: # 18 女
        # 向字典中添加键值对
        new_dict[k] = v
print(new_dict)

# todo 字典的推导式这么用！
new_dict = {
    k:v
    for k, v in zip(ks, vs)
}
print(new_dict) # {'age': 18, 'gender': '女'}
#  把ks列表和vs列表中的值，进行一一对应组合，返回可以遍历的对象
print(zip(ks, vs))


# todo 字符串
sr = '' # 空字符串
sr = "" # 空字符串
sr = "'" # 单引号字符串
sr = '"' # 双引号字符串
sr = '{1}' # 引号包裹的都是字符串
sr ='1\n2\n' # \n就是换行符——也是字符串
long_str = """多行字符串
"""

# 拼接字符串
sr1 = '你'
sr2 = '我'
print(sr1+sr2)

lst1 = [1]
lst2 = [2]
print(lst1+lst2)

tpl1 = (1,)
tpl2 = (2,)
print(tpl1+tpl2)

# todo 字符串、列表、元组 都有下标index，所以能够用+拼接
# 集合不能拼接
# st1 = {1}
# st2 = {2}
# print(st1 + st2)
# dt1 = {'a':1}
# dt2 = {'b':2}
# print(dt1+dt2)

# 字符串切片
print('123476'[::-1])

# 在字符串中查找目标字符串
print('123476'.find('123')) # 返回要查找字符串的起始下标
print('123476'.find('900')) # 返回的是-1表示找不到

# 替换
print('123476'.replace('6', '你好'))
# print('123476'.replace('6', '你好', 次数))

# 基于字符进行切，切完返回字符串构成的列表
print('123476'.split('4')) # ['123', '76']
# print('123476'.split('')) # 不可以！报错
lst = [v for v in '123476']
print(lst)
# lst = []
# for v in '123476':
#     lst.append(v)
# print(lst)

# sr = '123456789'
# ret_list = []
# for i, v in enumerate(sr):
#     # 下标是 0 1 2 3 4...
#     # 判断下标是偶数
#     if i % 2 == 0:
#         print(sr[i:i+2])
#         ret_list.append(sr[i:i+2])
# print(ret_list)

# 把字符串构成的列表拼接起来
print(''.join(lst))
# 把字符串构成的列表 用 '@' 拼接起来
print('@'.join(lst))

# 转成字符串
print(str(12345), type(str(12345))) # 12345 <class 'str'>
# 把字符串转换成别的类型，原字符串像啥就变成啥类型
a = '12345'
print(eval(a), type(eval(a))) # 12345 <class 'int'>

# 字符串可以查看字符的个数
print(len(''))
print(min('中国崛起ab1230')) # 字符串能够求最大最小值，但是没啥意义

# 字符串遍历
for v in a:
    print(v)
for i, v in enumerate(a):
    print(i, v)

# 判断字符串是否在目标字符串中
if '中国' in '中国崛起ab1230':
    print('存在')
if '美国' not in '中国崛起ab1230':
    print('不存在')

# todo 可变vs不可变 ：自身包含的元素是否可以改
""" 
list 可变
tuple 不可变
集合 可变
字符串 不可变
字典 可变
"""

# 集合无序，多运行几遍就知道了！
a = {'a', 'b', 'c'}
for i,v in enumerate(a):
    print(i,v)



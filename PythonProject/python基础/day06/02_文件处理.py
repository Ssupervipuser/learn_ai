
# f = open('1.txt', 'w')
# f.close()

# todo w 是写入模式
with open('1.txt', 'w') as f:
    f.write('要写的内容')

# todo r 是读模式
with open('1.txt', 'r') as f:
    result = f.read(3) # 参数：读取的字符数量
    print(result)
    result = f.read() # 不给参数：读取全部的内容
    # 多次执行f.read()函数时，继续向后读取
    print(result)
    # print( type(f.read()) )
    # todo 文件内容最后是 ''空字符串！
    print(1111)

# with open('2.txt', 'r') as f:
#     rets = f.readlines()
#     print(rets) # 每行内容作为一个元素、构成的列表

with open('2.txt', 'r') as f:
    ret = f.readline()
    print(ret) # 读取一行
    ret = f.readline()
    print(ret)  # 读取一行
    ret = f.readline()
    print(ret) # 读取一行
    ret = f.readline()
    print(ret)  # 读取一行

# 需求：用行读取的方式读取 00_作业.py 文件，打印每一行，直到读取打印完毕
with open('00_作业.py', 'r', encoding='utf8') as f:
    # 打印每一行，直到读取打印完毕
    while 1:
        ret = f.readline()
        # 读取一行，行末尾一定是个\n换行符
        # print函数默认换行
        # 两次换行，改成一次换行，end参数的值改为''空串
        print(ret, end='')
        # 退出循环的条件：读取的一行是一个''空字符串
        if ret == '':
            break

# 需求：用行读取的方式读取 00_作业.py 文件，打印每一行，直到读取打印完毕
with open('00_作业.py', 'r', encoding='utf8') as f:
    content_list = f.readlines()
    for content in content_list:
        print(content, end='')


with open('3.txt', 'w', encoding='utf8') as f:
    f.write('此文件编码格式是utf-8')

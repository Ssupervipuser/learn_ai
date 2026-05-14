import time, multiprocessing

# 全局变量
my_list = []

# 子进程任务1
def add_data():
    for i in range(3):
        my_list.append(i)
        print(f'add_data进程：添加{i}')
    print(f'add_data: {my_list}')

# 子进程任务2
def get_data():
    print(f'get_data: {my_list}')

if __name__ == '__main__':
    # 创建子进程对象
    add_p = multiprocessing.Process(target=add_data)
    get_p = multiprocessing.Process(target=get_data)

    # 启动子进程
    add_p.start() # add_data: [0, 1, 2]
    time.sleep(5)
    get_p.start() # get_data: [] todo 说明进程之间不共享变量
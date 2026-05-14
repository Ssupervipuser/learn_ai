import time, threading

# 全局变量
my_list = []

# 子线程任务1
def add_data():
    for i in range(3):
        my_list.append(i)
        print(f'add_data进程：添加{i}')
    print(f'add_data: {my_list}')

# 子线程任务2
def get_data():
    print(f'get_data: {my_list}')

if __name__ == '__main__':
    # 创建子线程对象
    add_t = threading.Thread(target=add_data)
    get_t = threading.Thread(target=get_data)

    # 启动子进程
    add_t.start() # add_data: [0, 1, 2]
    time.sleep(5)
    get_t.start() # get_data: [0, 1, 2] todo 说明线程之间共享全局变量

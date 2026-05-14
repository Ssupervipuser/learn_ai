import threading, time
# todo 下边代码证明：多线程的共享全局变量——不安全

# g_num = 0 # 全局变量
# def sum_num1():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print('sum1: ', g_num)
#
# def sum_num2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print('sum2: ', g_num)
#
# if __name__ == '__main__':
#     # 创建子线程对象
#     add_t = threading.Thread(target=sum_num1)
#     get_t = threading.Thread(target=sum_num2)
#
#     # 启动子进程
#     add_t.start()
#     get_t.start()

g_num = 0 # 全局变量
def sum_num1():
    global g_num
    for i in range(1000):
        temp = g_num
        time.sleep(0.0001)
        g_num = temp + 1
    print('sum1: ', g_num)

def sum_num2():
    global g_num
    for i in range(1000):
        temp = g_num
        time.sleep(0.0001)
        g_num = temp + 1
    print('sum2: ', g_num)

if __name__ == '__main__':
    # 创建子线程对象
    sum1_t = threading.Thread(target=sum_num1)
    sum2_t = threading.Thread(target=sum_num2)

    # sum1_t.daemon = True

    # 启动子进程
    sum1_t.start()
    sum2_t.start()

    # 线程执行完毕后再向下执行
    # sum1_t.join() # 阻塞的是主线程
    # sum2_t.join() # 阻塞的是主线程

    print(g_num)
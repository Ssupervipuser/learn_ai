import threading

g_num = 0 # 全局变量

lock = threading.Lock() # 创建锁

def sum_num1():

    global g_num
    for i in range(1000000):
        lock.acquire()  # 上锁
        g_num += 1
    print('sum_num1: ', g_num)
    lock.release() # 解锁

def sum_num2():
    lock.acquire() # 上锁
    global g_num
    for i in range(1000000):
        g_num += 1
    print('sum_num2: ', g_num)

if __name__ == '__main__':
    # 创建子线程
    t1 = threading.Thread(target=sum_num1)
    t2 = threading.Thread(target=sum_num2)
    # 线程启动
    t1.start()
    t2.start()


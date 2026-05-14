import threading, time

# todo 创建锁对象
lock = threading.Lock()

g_num = 0 # 全局变量
def sum_num1():
    global g_num
    for i in range(1000):
        lock.acquire() # todo 上锁、抢锁
        temp = g_num
        time.sleep(0.0001)
        g_num = temp + 1
        lock.release() # todo 解锁
    print('sum1: ', g_num)

def sum_num2():
    global g_num
    for i in range(1000):
        lock.acquire() # todo 上锁、抢锁
        temp = g_num
        time.sleep(0.0001)
        g_num = temp + 1
        lock.release() # todo 解锁
    print('sum2: ', g_num)

if __name__ == '__main__':
    # 创建子线程对象
    sum1_t = threading.Thread(target=sum_num1)
    sum2_t = threading.Thread(target=sum_num2)
    # 启动子进程
    sum1_t.start()
    sum2_t.start()

    print(g_num)
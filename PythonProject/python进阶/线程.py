# import threading
# import time
#
#
# def task():
#     time.sleep(1)
#     print("当前线程:", threading.current_thread().name)
#
#
# if __name__ == '__main__':
#
#    for _ in range(5):
#        sub_thread = threading.Thread(target=task)
#        sub_thread.start()


#
# import threading
# import time
#
#
# # 测试主线程是否会等待子线程执行完成以后程序再退出
# def show_info():
#     for i in range(5):
#         print("test:", i)
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     sub_thread = threading.Thread(target=show_info)
#     sub_thread.start()
#
#     # 主线程延时1秒
#     time.sleep(1)
#     print("over")

# import threading
#
# # 定义全局变量
# g_num = 0
#
#
# # 循环一次给全局变量加1
# def sum_num1():
#     for i in range(1000000):
#         global g_num
#         g_num += 1
#
#     print("sum1:", g_num)
#
#
# # 循环一次给全局变量加1
# def sum_num2():
#     for i in range(1000000):
#         global g_num
#         g_num += 1
#     print("sum2:", g_num)
#
#
# if __name__ == '__main__':
#     # 创建两个线程
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     # 启动线程
#     first_thread.start()
#     # 启动线程
#     second_thread.start()
#

#
# import threading ,time
#
# #todo 创建锁对象
# lock = threading.Lock()
# g_num = 0
# def sum_num1():
#     global g_num
#     for i in range(1000):
#         lock.acquire()  #todo 上锁，抢锁
#         temp=g_num
#         # time.sleep(0.001)
#         g_num=temp+1
#         lock.release()
#     print('sum1',g_num)
#
# def sum_num2():
#     global g_num
#     for i in range(1000):
#         lock.acquire()
#         temp=g_num
#         # time.sleep(0.001)
#         g_num=temp+1
#         lock.release()
#     print('sum2',g_num)
#
# if __name__ == '__main__':
#     #创建子线程对象
#     sum1_thread = threading.Thread(target=sum_num1)
#     sum2_thread = threading.Thread(target=sum_num2)
#
#     #启动子进程
#     sum1_thread.start()
#     sum2_thread.start()
#     # print(g_num)
#
#


# import threading
# import time
#
# # 创建互斥锁
# lock = threading.Lock()
#
#
# # 根据下标去取值， 保证同一时刻只能有一个线程去取值
# def get_value(index):
#
#     # 上锁
#     lock.acquire()
#     print(threading.current_thread())
#     my_list = [3,6,8,1]
#     # 判断下标释放越界
#     if index >= len(my_list):
#         print("下标越界:", index)
#         return
#     value = my_list[index]
#     print(value)
#     time.sleep(0.2)
#     # 释放锁
#     lock.release()
#
#
# if __name__ == '__main__':
#     # 模拟大量线程去执行取值操作
#     for i in range(30):
#         sub_thread = threading.Thread(target=get_value, args=(i,))
#         sub_thread.start()

import threading
g=0
lock=threading.Lock()
def work(t_name,n):
    global g
    for i in range(n):
        lock.acquire()
        g=g+1
        lock.release()
        print('线程：',t_name)
    print(g)

if __name__ == '__main__':
    t_list=[]
    for t_name in range(5):
        t=threading.Thread(target=work,args=(t_name,3))
        t_list.append(t)

    for t in t_list:
        t.start()

    for t in t_list:
        t.join()

    print(g)


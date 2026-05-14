"""
并发 ： 交替运行-多线程
并行 ： 真·同时运行-多进程
"""
import threading

g = 0
lock = threading.Lock() # 创建互斥锁

def work(t_name, n):
    global g
    for i in range(n):
        # 在操作全局变量的前后进行加锁、解锁
        lock.acquire() # 上锁
        g += 1
        lock.release() # 解锁
        print('线程', t_name)
    print(g)


if __name__ == '__main__':
    # 主线程才会执行这里
    t_list = []
    for t_name in range(5):
        t = threading.Thread(target=work, args=(t_name, 3))
        # t = threading.Thread(target=work, kwargs={'t_name': t_name, 'n':3 })
        # 设置守护进程：主死从立刻死
        # t.daemon = True
        t_list.append(t) # 子线程对象添加到列表中

    for t in t_list:
        # 子线程启动
        t.start()

    for t in t_list:
        # 阻塞主线程，直到子线程结束，才向下执行
        t.join()

    print(g)

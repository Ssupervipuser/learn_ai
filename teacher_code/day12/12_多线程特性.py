import threading
import time

def get_info():
    time.sleep(0.5)
    # 获取当前线程信息
    current_thread = threading.current_thread()
    print(current_thread)
    # <Thread(Thread-2 (get_info), started 14964)>

def work():
    for i in range(10):
        print('working...')
        time.sleep(0.2)


if __name__ == '__main__':
    print('*'*10, '多线程无序')
    # for i in range(10):
    #     t = threading.Thread(target=get_info)
    #     t.start()
    print('*' * 10, '主线程默认等待子线程结束再结束')
    wt = threading.Thread(target=work)
    # 和子进程一样，设置子线程为守护线程
    wt.daemon = True # 主死从立刻死

    wt.start()
    time.sleep(1)
    print('主线程结束')
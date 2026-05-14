import multiprocessing
import time


def work():
    for i in range(10):
        print('工作...')
        time.sleep(0.2)

if __name__ == '__main__':
    wp = multiprocessing.Process(target=work)

    # todo 主进程默认会等待子进程结束后再结束
    #  进程对象.daemon=True 这就让主进程结束、子进程也结束
    #  主进程不再等待子进程结束才结束
    # 设置子进程为守护进程
    # wp.daemon = True # 主死从立刻死

    print(111)
    wp.start()
    time.sleep(2)
    # 立刻终止子进程，主进程没有子进程了、该结束就结束了
    wp.terminate()

    wp.join() # 回收子进程资源
    time.sleep(3)
    # 阻塞主进程程序的运行，回收子进程资源

    print(222)

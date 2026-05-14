import multiprocessing
import time


def work():
    for i in range(10):
        print('工作...')
        time.sleep(2)

if __name__ == '__main__':
    wp = multiprocessing.Process(target=work)

    # todo 主进程默认会等待子进程结束后再结束
    #  进程对象.daemon=True 这就让主进程结束、子进程也结束
    #  主进程不再等待子进程结束才结束
    # 设置子进程为守护进程
    wp.daemon = True # 主死从立刻死

    print(111)
    wp.start()

    print(222)

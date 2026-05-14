import multiprocessing
import time

# 定义子进程任务函数
def work(n, pname):
    for i in range(n):
        # time.sleep(0.3)
        print(pname, ': ', i, '...')


if __name__ == '__main__':
    # 这里的代码只有主进程才会执行！
    wp_list = []
    for i in range(3):
        pname = '子进程 ' + str(i) # 子进程 1
        # 创建子进程对象
        # wp = multiprocessing.Process(target=work, args=(10, pname))
        wp = multiprocessing.Process(target=work, kwargs={'n':3, 'pname':pname})
        # 设置子进程为守护进程：主死子立刻也死
        # wp.daemon = True

        wp_list.append(wp) # 把创建的子进程对象 添加到列表中

    # 依次开始执行所有的子进程
    for wp in wp_list:
        wp.start()
        # print(111)
        # time.sleep(1.2)
        # print(222)
        # 主动让子进程结束
        # wp.terminate()
        # wp.join() # 阻塞：等待子进程运行结束，程序才向下执行
        # print(111)
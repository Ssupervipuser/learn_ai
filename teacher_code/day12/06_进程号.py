import os
import time
import multiprocessing

print('主进程、子进程都会执行我！')
# 子进程任务函数1
def coding(n, name):
    for i in range(n):
        print('{}写代码'.format(name))
        time.sleep(0.3)
    print(os.getpid(), os.getppid()) # 当前进程号，父进程号
    print(multiprocessing.current_process().pid) # 当前进程号


# 子进程任务函数2
def music(c, name):
    for i in range(c):
        print('{}听音乐'.format(name))
        time.sleep(0.3)
    print(os.getpid(), os.getppid()) # 当前进程号，父进程号
    print(multiprocessing.current_process().pid) # 当前进程号


# todo 子进程一旦运行会立刻把父进程代码复制并执行！
if __name__ == '__main__':
    # todo 这个代码区的代码只有主进程（父进程）才执行
    # 创建子进程对象
    # target=子进程要执行的工作函数名
    coding_process = multiprocessing.Process(
        target=coding,
        args=(5, '小明') # 向target指向的函数传参
    )
    music_process = multiprocessing.Process(
        target=music,
        # 向target指向的函数传参
        # k是形参，v是实参
        kwargs={'c':3, 'name':'小明'}
    )

    # 启动子进程
    coding_process.start()
    music_process.start()

    # 获取当前进程的id
    print(os.getpid())
    print(multiprocessing.current_process().pid)
    # 获取父进程id
    print(os.getppid())



import multiprocessing # 多进程导包
import time

def coding(n, name):
    for i in range(n):
        print('{}写代码'.format(name))
        # time.sleep(0.3)

def music(c, name):
    for i in range(c):
        print('{}听音乐'.format(name))
        # time.sleep(0.3)

if __name__ == '__main__':
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



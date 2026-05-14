import multiprocessing
import time
import os

def coding(n,name):
    for i in range(n):
        print('{}写代码'.format(name))
        time.sleep(0.3)

def music(c,name):
    for i in range(c):
        print('{}听音乐'.format(name))
        time.sleep(0.3)

if __name__ == '__main__':
    coding_process=multiprocessing.Process(
    target=coding,
    args=(3,'小明')
    )
    music_process=multiprocessing.Process(
    target=music,
    kwargs={'c':3,'name':'小明'}
    )

    coding_process.start()
    pid=os.getpid()
    print(pid)

    music_process.start()
    pid=os.getpid()

    print(pid)
    ppid=os.getppid()
    print(ppid)

import multiprocessing # 多进程导包
import time


def coding():
    for i in range(3):
        print('写代码')
        time.sleep(0.3)

def music():
    for i in range(3):
        print('听音乐')
        time.sleep(0.3)

if __name__ == '__main__':


    # 创建子进程对象
    # target=子进程要执行的工作函数名
    coding_process = multiprocessing.Process(target=coding)
    music_process = multiprocessing.Process(target=music)

    # 启动子进程
    coding_process.start()
    music_process.start()
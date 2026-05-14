import threading # 多线程包
import time

def coding(n, name):
    for i in range(n):
        print(f'{name} coding...')
        time.sleep(0.3)

def music(n, name):
    for i in range(n):
        print(f'{name} music...')
        time.sleep(0.3)

if __name__ == '__main__':
    # 创建子线程对象
    coding_thread = threading.Thread(target=coding, args=(3, '张三'))
    music_thread = threading.Thread(target=music, kwargs={'n':4, 'name':'李四'})
    # 启动子线程
    coding_thread.start()
    music_thread.start()
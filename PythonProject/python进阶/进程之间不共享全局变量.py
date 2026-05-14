import multiprocessing
import time
#
# my_list=[]
#
# #写入数据
# def write_data():
#     for i in range(3):
#         my_list.append(i)
#         print("add",i)
#     print('写入完成',my_list)
#
# def read_data():
#     print('读取数据',my_list)
#
# if __name__ == '__main__':
#     wp=multiprocessing.Process(target=write_data)
#     rp=multiprocessing.Process(target=read_data)
#     wp.start()
#     time.sleep(1)
#     rp.start()


# def work():
#     for i in range(10):
#         print('working')
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     wp=multiprocessing.Process(target=work)
#     wp.start()
#
#     time.sleep(0.5)
#     print('主进程执行完毕')
    # wp=multiprocessing.Process(target=work)
    # wp.daemon=True
    # print('start')
    # wp.start()
    #
    # time.sleep(1)
    # print('主进程执行完毕')



# 默认主进程会等待所有的子进程执行结束再结束
import multiprocessing
import time

# 工作函数
def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    work_process = multiprocessing.Process(target=work)
    # 启动子进程
    work_process.start()
    # 延时1秒
    time.sleep(1)
    print("主进程执行完毕")
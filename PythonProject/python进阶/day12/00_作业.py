# todo 1. 代码 02_tcp....py
#1.创建服务端套接字对象
# import socket
#
# tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #设置端口复用
# tcp_server_socket.setsockopt(
#     socket.SOL_SOCKET,
#     socket.SO_REUSEADDR,    #是否复用端口号
#     True
# )
# #2.绑定IP和端口号
# tcp_server_socket.bind(("",8888))
# #'127.0.0.1'表示本地开放
# #’0.0.0.0.0‘和''表示公开广播，谁都可以访问我
#
# #3.监听，5表示服务端等待排队的链接最大数量
# tcp_server_socket.listen(5)

#服务端一致不停的处理新的客户消息
# while True:
#     #4.等待服务端连接请求
#     conn, ip_port = tcp_server_socket.accept()
#     #conn他是专门和客户端连接的socket对象
#     print('客户端ip端口是：',ip_port)
#
#     try:
#         #5.接收数据
#         recv_data=conn.recv(1024)
#         print(recv_data.decode('utf-8'))
#         #6.主动给客户端发消息
#         conn.send('客户端，你的消息我收到了，我是服务器'.encode('utf-8'))
#     except Exception as e:
#         print(e)
#         conn.close()


# todo 2. 代码 10_多进程....py

import multiprocessing ,time
#定义子进程任务函数
def work(n,pname):
    for i in range(n):
        print(pname,':',i,'....')

if __name__ == '__main__':
    #这里的代码只有主进程才会执行
    wp_list=[]
    for i in range(3):
        pname='子进程'+str(i)
        #创建子进程对象
        # wp=multiprocessing.Process(target=work,args=(3,pname))
        wp=multiprocessing.Process(target=work,kwargs={'n':3,'pname':pname})

        #设置守护进程
        #wp.daemon=True
        wp_list.append(wp)  #把创建的子进程 对象，添加到列表中

    #依次开始执行所有的子进程
    for wp in wp_list:
        wp.start()

# todo 3. 代码 17_多线程....py 写多线程代码



# todo 4. 中文文字说明 多线程共享的全局变量为啥会出现数据错误的现象



# todo 5. 多线程互斥锁 15_互斥锁.py


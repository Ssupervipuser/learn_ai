import socket
import traceback

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# todo 设置端口复用
tcp_server_socket.setsockopt(
    socket.SOL_SOCKET,  # 当前的socket对象
    socket.SO_REUSEADDR, # 是否复用端口号？
    True # 是！
)

# 2. 绑定IP和端口
tcp_server_socket.bind(('', 8888))
# '127.0.0.1' 表示本地开放
# '0.0.0.0' 表示公开广播，谁都可以访问我
# '' 表示公开广播，谁都可以访问我

# 3. 监听，5表示服务端等待排队的连接的最大数量
tcp_server_socket.listen(5)

# todo 然服务端一直不停地处理新的客户的消息
while True:
    # 4. 等待服务端连接请求
    # conn_socket 他是专门和客户端连接的socket对象
    conn_socket, ip_port = tcp_server_socket.accept()
    print('客户端的IP端口是：' ,ip_port)

    try:
    # 5. 接收数据
        recv_data = conn_socket.recv(1024)
        print(recv_data.decode('utf8'))
        # 6. 主动给客户端发消息
        conn_socket.send('客户段、你的消息我收到了，我是服务器'.encode('utf8'))
    except:
        print(traceback.format_exc())
        # 7. 关闭套接字
        conn_socket.close()


# tcp_server_socket.close()
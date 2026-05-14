import socket

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定IP和端口
tcp_server_socket.bind(('127.0.0.1', 8888))

# 3. 监听，5表示服务端等待排队的连接的最大数量
tcp_server_socket.listen(5)

# 4. 等待服务端连接请求
# conn_socket 他是专门和客户端连接的socket对象
conn_socket, ip_port = tcp_server_socket.accept()
print('客户端的IP端口是：' ,ip_port)

# 5. 接收数据
recv_data = conn_socket.recv(1024)
print(recv_data.decode())

# 6. 主动给客户端发消息
conn_socket.send('客户段、你的消息我收到了，我是服务器'.encode())

# 7. 关闭套接字
conn_socket.close()
tcp_server_socket.close()
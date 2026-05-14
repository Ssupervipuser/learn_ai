import socket

# 1. 创建客户端的套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 和服务端套接字建立连接
tcp_client_socket.connect(
    # 目标服务器的ip地址, 目标服务器服务端的端口号
    ('127.0.0.1', 8888)
)

# 3. 发消息
tcp_client_socket.send('你好！'.encode())

# 4. 接收
recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode())

# 5. 关闭
tcp_client_socket.close()
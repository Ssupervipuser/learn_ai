
import socket

# 创建用于tcp连接的socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(tcp_socket)
print(type(tcp_socket))
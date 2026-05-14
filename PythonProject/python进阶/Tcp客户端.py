import socket
#1.创建客户端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.和服务端套接字建立链接
tcp_client_socket.connect(('127.0.0.1', 8888))

#3.发送数据
tcp_client_socket.send('Hello World!'.encode('utf-8'))
#4.接收数据，等待数据的到来
recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode())

tcp_client_socket.close()
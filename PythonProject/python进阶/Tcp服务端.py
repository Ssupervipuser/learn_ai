import socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.绑定端口和端口号
tcp_server_socket.bind(('', 8888))
#3.设置监听，代表服务端等待排序连接的最大数量
tcp_server_socket.listen(128)

#4.等待接收客户端的链接请求 accept阻塞等待，返回一个用于和客户端通讯socket，客户端地址
conn, addr = tcp_server_socket.accept()

#5.接收数据
recv_data = conn.recv(1024)
print("接收到的数据",recv_data.decode())

#6.发送数据
conn.send('客户端你的数据我收到了'.encode())

#5.关闭客户端套接字
conn.close()
tcp_server_socket.close()




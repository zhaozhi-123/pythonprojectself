"""
服务器端开发流程：
    1.创建服务器端Socket对象
    2.连接服务器端，指定：服务器端IP地址和端口号
    3.接收客户端的信息并打印
    4.给服务器端发送消息
    5.释放资源


客户端和服务器端是通过字节流（bytes）的形式实现的
"""

#1.导包
import socket

# 1.创建服务器端Socket对象，ipv4，TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.连接服务器端，指定：服务器端IP地址和端口号
client_socket.connect(("127.0.0.1",8888))
# 3.接收客户端的信息并打印
data = client_socket.recv(1024).decode("UTF-8")
print(f"客户端收到：{data}")
# 4.给服务器端发送消息
client_socket.send("Socket有趣!".encode("UTF-8"))

# 5.释放资源
client_socket.close()
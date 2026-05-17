"""
Socket通信，即通信双方都独有自己的Socket对象
数据在Socket之间通过，数据报包（UDP协议）或字节流（TCP协议）的形式进行传输
"""
import socket

#创建Socket对象
#参1：Address Family，地址族，即Ipv4还是Ipv6 默认值：AF_INET(ipv4) AF_INET(ipv6)
#参2：SocketType，Socket类型，即TCP还是UDP，默认值：SOCK_STREAM(TCP) SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)













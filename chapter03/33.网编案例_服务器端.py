"""
服务器端开发流程：
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数（1-128），一般为5
    4.等待客户端申请建立连接
    5.给客户端发送消息
    6.接收客户端的信息并打印
    7.释放资源


客户端和服务器端是通过字节流（bytes）的形式实现的
"""

#1.导包
import socket

#2.创建服务器端的Socket对象，ipv4，字节流（TCP）
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#3.绑定IP地址和端口号
server_socket.bind(('127.0.0.1', 8080))
#4.设置最大监听数
server_socket.listen(5)
while True:
    try:
        #5.等待客户端申请建立连接
        # print(1)
        accept_socket, client_info = server_socket.accept()
        # print(2)
        #6.给客户端发送消息
        accept_socket.send(b"Welcome To Socket!")#b 转为二进制（有中文不行）
        #7.接收客户端信息并打印
        data=accept_socket.recv(1024).decode("UTF-8")
        print(f"服务器收到：来自{client_info}的信息：{data}")
        #8.释放资源
        accept_socket.close()
        # server_socket.close() #服务器端一般不关闭
    except:
        pass

#扩展：设置端口号重用，目的是：快速重启服务器（服务器关闭后，立即释放端口）
#参1：当前的套接字对象，   参2：选项名      参3：该选项的值
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

"""
编码："字符串".encode(码表)
解码："字符串".decode(码表)

乱码唯一原因：编解码不同

英文字母，数字，特殊符合无论什么码表都只占一个字符，中文在utf-8(默认)占3个字节，在gbk占2个字节

二进制数据特殊写法，即 : b" 字母 数字 特殊符号 "，该方式对于中文无效
"""



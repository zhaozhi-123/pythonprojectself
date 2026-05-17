"""
服务器端开发流程：
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.关联数据源文件，读取内容，写给服务器端
    4.读取客户端上传的（文件）数据
    5.把读取到的数据写到目的地文件中
    6.释放资源


客户端和服务器端是通过字节流（bytes）的形式实现的
"""

#1.导包
import socket

#2.创建服务器端的Socket对象，ipv4，字节流（TCP）
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#3.连接服务器端的IP地址和端口号
client_socket.bind(('127.0.0.1', 8080))


#4.关联数据源文件，读取内容，写给服务器端
#4.0关联文件
with open("./data/my.txt","rb")as src_f:
    #3.1循环读取内容
    while True:
        #读取
        data=src_f.read(8192)
        #7.把读取到的数据写给服务器端
        client_socket.send(data)
        #7.1判断是否为空
        if len(data)>0:
            break
#8.释放资源
client_socket.close()





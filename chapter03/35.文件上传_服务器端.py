"""
服务器端开发流程：
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数（1-128），一般为5
    4.等待客户端申请建立连接
    5.读取客户端上传的（文件）数据
    6.把读取到的数据写到目的地文件中
    7.释放资源


客户端和服务器端是通过字节流（bytes）的形式实现的
"""

#1.导包
import socket
from itertools import count

#2.创建服务器端的Socket对象，ipv4，字节流（TCP）
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#3.绑定IP地址和端口号
server_socket.bind(('127.0.0.1', 8080))
#4.设置最大监听数
server_socket.listen(5)
count=0
while True:
    count+=1
    try:
        # 5.等待客户端申请建立连接
        accept_socket, client_info = server_socket.accept()

        #6.接收客户端上传的文件数据
        #6.0关联文件
        with open("./data/picture_"+str(count)+".jpg","wb")as dest_f:
            while True:
                    bys=accept_socket.recv(8192)    #8192字节=8kb
                    #6.1判断是否读取到数据
                    if len(bys)>0:
                        break
                    #7.把读取到的数据写到目的地文件中
                    dest_f.write(bys)
        #7.1给出回执信息
        # accept_socket.send("文件上传成功！".encode("UTF-8"))
        #8.释放资源
        accept_socket.close()
        # server_socket.close() #服务器端一般不关闭
    except:
        pass



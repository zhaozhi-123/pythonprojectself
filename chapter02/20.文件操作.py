#相对路径写法
# f1=open("hi.txt","r",encoding="utf-8")
#绝对路径写法
# f2=open("E:\pythonproject\pythonprojectself\chapter02/hi.txt","r",encoding="utf-8")
#
#r只读
#w写入
#a追赶

################   文件读取 read  ###############
# content=f1.read() #读取全部
# print(content)
#
# content=f1.read(3) #读3个长度
# print(content)
#
# #readlines 按行一次性读取，返回列表，每一行数据为一个元素
# lst=f1.readlines()
# for line in f1.readlines: #readlines每行的换行\n不会清除
#     line=line.strip() #去除首尾的空格和回车
#     print(line)
# print(lst)
# print(type(lst))
#
#readline 一次读取一行 \n不会去掉
# print(f1.readline())
# print(f1.readline().strip())

# for line in f1: #/for line in f1.readlines():/#for line in open(E:/hi):
#     print(line.strip())#自行处理\n

# with open("hi.txt","w",encoding="utf-8") as f1: #不需要写close，会自动调用

#close
# f1.close()

#统计文件，统计指定单词出现次数
# num=0
# f1=open("hi.txt","r",encoding="utf-8")
#
# for line in f1.readlines():
#     line=line.strip()
#     for word in line.split():
#         if "word"==word:
#             num+=1
#
# f1.close()
# print(f"文件里有{num}个word")

###############  文件写入 write :清空原有内容 ##################
# import time
#
# s=time.time()
# f=open("hi.txt","w",encoding="utf-8")
#
# for i in range(100):
#     f.write(str(i)+"\n")
#     # f.flush()
#
# f.close() #自带flush功能
# end=time.time()
# print(end-s)

###############  文件追加 append :追加新内容 ##################
# f=open("hi.txt","a",encoding="utf-8")
#
# f.write("哈哈哈\n") #write不会自带换行
#
# f.close()

###############  非文本文件操作：二进制处理 b ###########
# fr=open("D:/hi.mp4","rb") #二进制读
# fw=open("E:/hi.mp4","wb") #二进制写
#
# content=fr.read()
# fw.write(content)
#
# fr.close()
# fw.close()


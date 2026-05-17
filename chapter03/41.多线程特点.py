# """
# 案例：演示多线程特点
#
# 多线程特点：
#     1.线程执行具有随机性，原因为CPU做高效切换
#     2.默认情况下，主线程会等待子线程结束再结束
#     3.（同一个进程的）线程间 数据共享
#     4.多线程操作共享数据，可能出现安全问题，可以用互斥锁解决
#
# CPU调度资源的策略
#     1.均分时间片
#     2.抢占式调度
# """
#
#
# ################守护线程##################
# import threading, time
#
# def work():
#     for i in range(10):
#         time.sleep(0.1)
#         print("工作中。。。")
#
# if __name__ == "__main__":
#     #创建子线程对象
#     #守护线程写法1：daemon属性
#     # t=threading.Thread(target=work,daemon=True)
#
#     #守护线程写法2：setDaemon()函数，已过时（暂支持）
#     # t = threading.Thread(target=work)
#     # t.setDaemon(True)
#
#     # 守护线程写法3：daemon属性
#     t=threading.Thread(target=work)
#     t.daemon = True
#
#     #启动线程
#     t.start()
#
#     #设置主线程休眠时间1秒
#     time.sleep(1)
#     #设置主线程结束标记
#     print("主线程已经结束")
#
# ################线程间数据共享##################
# import threading, time
#
# #定义全局变量
# my_list=[]
#
# #定义目标函数，添加数据
# def write_data():
#     for i in range(1,6):
#         my_list.append(i)
#         print("写入数据：",i)
#         print(f"write_data函数：{my_list}")
#
# #定义目标函数，查看数据
# def read_data():
#     time.sleep(2)
#     print(f"read_data函数：{my_list}")
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=write_data)
#     t2 = threading.Thread(target=read_data)
#
#     t1.start()
#     t2.start()
#
#
####################互斥锁##################
import threading

global_num = 0

#创建锁对象
mutex=threading.Lock()


def target_fun1():
    mutex.acquire()
    #声明为全局变量
    global global_num
    for i in range(1000):
        global_num += 1

    print(f"target_fun1函数结果：{global_num}")
    mutex.release()     #释放锁

def target_fun2():
    mutex.acquire()
    #声明为全局变量
    global global_num
    for i in range(1000):
        global_num += 1

    print(f"target_fun1函数结果：{global_num}")
    mutex.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=target_fun1)
    t2 = threading.Thread(target=target_fun2)

    t1.start()
    t2.start()

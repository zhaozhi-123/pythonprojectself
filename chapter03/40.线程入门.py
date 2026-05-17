"""
1.进程是CPU分配资源的基本单位
  线程是CPU调度资源的最小单位

2.线程依附于进程，每个进程至少有1个线程（主程序栈）

3.进程间数据相互隔离，（同一个进程的）线程间数据可以共享
"""

import threading
import time

def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print("正在敲第{i}行代码。。。")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print("正在听第{i}首音乐。。。")

if __name__ == '__main__':

    t1 = threading.Thread(target=coding,args=("李想",100))
    t2 = threading.Thread(target=music,kwargs={"count":50,"name":"周力"})

    #main中函数优先执行
    # for i in range(5):
    #     time.sleep(0.1)
    #     print("main")

    t1.start()
    t2.start()


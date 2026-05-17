"""
    进程之间数据相互隔离，子进程会将父进程的main外资源拷贝一份

    默认情况下，主进程会等待子进程执行结束再结束
    思路1：设置子进程为守护进程      /p1.daemon=True
    思路2：强制关闭子进程         /p.terminate

"""
import multiprocessing
import time

my_list=[]

def write_data():
    for i in range(1,6):
        my_list.append(i)
        print(f"添加数据：{i}")

    print(f"write_data函数:{my_list}") #{1，2，3，4，5}

def read_data():
    time.sleep(3)
    print(f"read_data函数:{my_list}")

if __name__ == '__main__':
    p1=multiprocessing.Process(target=write_data,name="write_data")
    p2=multiprocessing.Process(target=read_data)
    print(f"p1进程的名字:{p1.name}")

    p1.start()
    p2.start()
    print("main内资源，观察执行几次")
"""
方式一：args方式，接受所有的位置参数

方式二：kwargs方式，接受所有的关键字参数
"""
import multiprocessing
import os


def coding(name,num):
    for i in range(1,num+1):
        print(f"{name}正在敲第{i}遍代码。。。")
    # print(f"p1进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid为):{os.getppid()}")


def music(name,count):
    for i in range(1,count+1):
        print(f"{name}正在听{i}遍歌曲。。。")

if __name__=="__main__":
    p1=multiprocessing.Process(target=coding,args=("虚竹",10))
    # p2=multiprocessing.Process(target=music,args=("刘备",20))
    p2=multiprocessing.Process(target=music,kwargs={"count":20,"name":"刘备"})
    # p2=multiprocessing.Process(target=music,kwargs={"name":"刘备","count":"20"})


    p1.start()
    p2.start()

    """
    查看当前进程id：
        os.getpid()
        multipocessing.current_process().pid
        
        查看当前进程的ppid:    parent process id
            os.getppid()
            
    main中创建的进程，若无特殊指定，父进程都是main进程
    main进程的父进程是Pycharm
    """
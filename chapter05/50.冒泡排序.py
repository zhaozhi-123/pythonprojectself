"""
冒泡排序：
    要点：比较的总轮数（i=n-1）
        每轮比较的总次数(j=n-1-轮数)
        谁和谁比较

    时间复杂度：
            最好：
            最坏：
    冒泡排序：稳定排序算法
"""

def bubble_sort(my_list):
    #获取列表长度
    n = len(my_list)
    #外循环，控制比较的轮数
    for i in range(n-1):
        for j in range(n-i-1):
            #交换过程 a,b=b,a
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

if __name__ == '__main__':
    my_list=[1,5,2,4,6,3]
    #调用函数
    bubble_sort(my_list)    #实参，可变
    #打印结果
    print(my_list)
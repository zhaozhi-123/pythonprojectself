"""
冒泡排序： 两两比较 逆序交换（交换位置） 每轮选择最大的值 后置
    要点：比较的总轮数（i=n-1）
        每轮比较的总次数(j=n-1-轮数)
        谁和谁比较

    时间复杂度：
            最好：O(n)
            最坏：O(n^2)
    冒泡排序：稳定排序算法

    外循环 -1:减少比较的轮数，提高效率
    内循环 -1:防止索引越界
    内循环 -i:减少每轮比较的轮数，提高效率
"""

def bubble_sort(my_list):
    #获取列表长度
    n = len(my_list)
    #外循环，控制比较的轮数
    for i in range(n-1):
        count = 0
        for j in range(n-i-1):
            #具体比较过程
            if my_list[j] > my_list[j+1]:
                count +=1
                # 交换过程 a,b=b,a
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

        print(f'第{i+1}轮交换了{count}次')

        if count==0:
            break
if __name__ == '__main__':
    my_list=[1,5,2,4,6,3]
    #调用函数
    bubble_sort(my_list)    #实参，可变
    #打印结果
    print(my_list)
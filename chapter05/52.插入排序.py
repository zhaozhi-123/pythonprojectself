"""
插入排序：（类冒泡，但每次交换不确定位置）列表两分，一有序，一无序，每次从无序中获取一个元素，与前边所有元素比较，决定位置，进行插入
时间复杂度：最好：O（n）
          最坏：O（n^2）
稳定算法
适用于少量数据
"""

#定义插入函数
def insert_sort(my_list):
    #获取列表长度
    n=len(my_list)          #n=5
    #外循环，控制比较的轮数
    for i in range(1,n):    #i的值：1，2，3，4
        #内循环，控制每轮比较的总次数
        for j in range(i,0,-1):    #j的值：1，2，3，4
            if my_list[j]<my_list[j-1]:
                my_list[j],my_list[j-1]=my_list[j-1],my_list[j]
            else:
                break

if __name__ == '__main__':
    my_list=[1,5,2,4,6,3]
    #调用函数，进行排序
    insert_sort(my_list)    #实参，可变
    #打印结果
    print(my_list)


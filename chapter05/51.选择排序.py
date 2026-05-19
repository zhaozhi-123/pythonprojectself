"""
选择排序：两两比较（不换位置），仅选出小值  最小置前置
时间复杂度：O（n^2）
"""
def select_sort(my_list):
    n=len(my_list)
    for i in range(n-1):
        min_index=i
        #内循环，选择最小值
        for j in range(i+1,n):
            #比较，索引min_index（初值i）和索引j比较
            if my_list[j]<my_list[min_index]:
                min_index=j     #记录最小值索引
        #已找到了最小值，换位置
        if min_index!=i:
            my_list[i],my_list[min_index]=my_list[min_index],my_list[i]

#测试
if __name__ == '__main__':
    my_list=[1,5,2,4,6,3]
    #调用函数
    select_sort(my_list)    #实参，可变
    #打印结果
    print(my_list)

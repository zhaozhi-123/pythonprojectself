"""
    快速排序：
    时间复杂度：
            平均/最好：O(nlog n)
            最坏：O(n^2)

"""

def quick_sort(my_list,start,end):
    """

    :param my_list: 要操作的列表
    :param start: 操作的元素，起始索引
    :param end: 操作的数据，结束索引
    :return:
    """
    #核心细节：若start >= end,则列表中只有一个元素，直接返回
    if start >= end:
        return

    #定义变量left和right,表示分界值左，右的索引
    left = start
    right = end
    #定义变量mid,表示分界值,假设列表的起始值为分界值
    mid=my_list[start]
    #具体的查找过程
    while left < right:
        while left < right and my_list[right] >= mid:
            right -= 1
        #找到比分界值小的元素
        my_list[left] = my_list[right]

        while left < right and my_list[left] < mid:
            left += 1
        my_list[right] = my_list[left]
    #循环结束，分界值已经找到，赋值
    my_list[left] = mid

    #递归调用，处理左右两边的元素
    quick_sort(my_list,start,left-1)
    quick_sort(my_list,right+1,end)

if __name__ == '__main__':
    my_list=[5,4,3,2,1]
    print(f'排序前：{my_list}')
    quick_sort(my_list,0,len(my_list))
    print(f'排序后：{my_list}')
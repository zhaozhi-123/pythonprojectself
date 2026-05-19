"""
二分查找：列表必须有序
    时间复杂度：O(log n)
"""
# 二分查找，递归版
def binary_search_recursion(my_list,target):
    """
    二分查找递归版
    :param my_list:待查找的列表
    :param target: 要查找的元素
    :return: True ：在
    """
    #获取列表长度
    n = len(my_list)
    #判断列表是否为空
    if n == 0:
        return False
    #获取列表的中值索引
    mid = n // 2
    #比较要查找的元素和中值
    if my_list[mid] == target:
        return True
    elif my_list[mid] > target:
        # 递归调用
        return binary_search_recursion(my_list[:mid], target)
    else:
        # 递归调用
        return binary_search_recursion(my_list[mid+1:], target)
    return  False

#二分查找，非递归版
def binary_search(my_list,target):
    #定义变量start,end
    start = 0
    end = len(my_list) - 1

    #循环查找
    while start <= end:
        #计算中值索引
        mid = (start + end) // 2
        #比较要查找的元素和中值
        if my_list[mid] == target:
            return True
        elif my_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return  False
if __name__ == '__main__':
    my_list = [2,3,9,13,23,31,55,77,99]
    print(binary_search_recursion(my_list, 23))#True
    print(binary_search_recursion(my_list, 25))#False
    print("-"*23)

    print(binary_search(my_list, 23))#True
    print(binary_search(my_list, 25))#False


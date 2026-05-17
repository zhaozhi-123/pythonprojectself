# #函数定义 ---先定义再调用
#
# def out_line():
#     print("----------")
#
# #函数调用 ---执行逻辑
# out_line()
import math


#函数的参数与返回值
#函数1：计算园的面积
# def circle_area(r):
#     area = 3.14 * (r ** 2)
#     return area
#
# circle = circle_area(10)
# print(circle)

#函数2：长方形的面积
# def rectangle_area(l,w):
#
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l:长度
#     :param w:宽度
#     :return:长方形的面积
#     """
#     area = l * w
#     return area
#
# # help(rectangle_area)
# print(rectangle_area(10,20))

#函数3：计算圆的面级，周长 --逗号分隔返回值 round(,1)保留一位小数
# def circle_area_len(r):
#
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(3.14 * (r * r),1),round(2*3.14*r,1)
#
# al=circle_area_len(5)
# print(al)
# print(type(al))


#解包
# area,len=circle_area_len(5)
# print(area)
# print(len)

#函数的嵌套调用
def function_a():
    print('function_a_before')
    function_b()
    print('function_a_after')

def function_b():
    print('function_b_before')
    function_c()
    print('function_b_after')

def function_c():
    print('function_c')

function_a()
print("函数调用完毕")
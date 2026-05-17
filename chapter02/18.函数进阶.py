# #全局变量
# num=100
#
# #定义函数
# def circle_area(r):
#     #局部变量：只能在函数内部使用
#     pi=3.14
#     area=pi*r*r
#     global num
#     num=10000
#     return area
#
# #调用函数
# c_area=circle_area(10)
# print(c_area)
#
# print(num)

#传惨方式
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名：{name}，年龄：{age},性别：{gender},城市{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# #传参方式1：位置参数
# stu=reg_stu("张三","20","男","上海")
# print(stu)
#
# #传参方式2：关键字参数
# stu=reg_stu(name="张三",age="20",gender="男",city="上海")
# print(stu)
#
# #传参方式3:混合参数
# stu=reg_stu("张三","20",gender="男",city="上海")
# print(stu)


#默认参数
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功，姓名：{name}，年龄：{age},性别：{gender},城市：{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# stu=reg_stu("王林",18)
# print(stu)

# stu=reg_stu("李幕婉","18","女")
# print(stu)
#
# stu=reg_stu("韩立","18",city="上海")
# print(stu)

#不定长参数（位置传递 *args-->元组）
#需求：根据传入数据，计算这批数据的最小值，最大值，平均值
# def calc_data(*args):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return (f"最小值为：{min_data},最大值为：{max_data},平均值为：{round(avg_data, 2)}")
#
# #调用函数
# print(calc_data(2,4,5,7,42,23,13,23))
#
# print(calc_data(2,4,5,7,42,23,13,23,254,215))
#

#不定长参数（关键字传递 **kwargs-->字典）
def calc_data(*args,**kwargs):
    """
    根据传入数据，计算这批数据的最小值，最大值，平均值
    :param args:不定长位置参数
    :param kwargs:不定长关键字参数
        round:保留的小数位个数
        print:是否打印输出
    :return:
    """
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data=round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值为：{min_data},最大值为：{max_data},平均值为：{round(avg_data, 2)}")


    return (f"最小值为：{min_data},最大值为：{max_data},平均值为：{avg_data, 2}")

#调用函数
# print(calc_data(2,4,5,7,42,23,round=3,print=True))

print(calc_data(2,4,5,7,42,23,13,23,254,215,round=1))


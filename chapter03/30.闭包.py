#定义函数，保存变量10
# def func1():
#     num=10
#     return num
#
# #调用函数，获取返回值
# num=func1()
# print(num+1) #11
# print(num+1) #11
# print(num+1) #11

#闭包解释：内部函数使用了外部函数的变量
"""格式：
    def 外部函数名（形参列表）：
        外部函数的（局部）变量

        def 内部函数名（形参列表）：
            使用外部函数的变量

        return 内部函数名

    前提条件：
        1.有嵌套       外部函数嵌套内部函数
        2.有引用       内部函数使用外部函数的变量
        3.有返回       外部函数中，返回 内部函数名（对象）
函数名：表示函数对象
函数名():表示调用函数，获取返回值
"""

# #函数名->是对象
# def get_sum(a,b):
#     return a+b
# print(get_sum)
# print(get_sum(2,3))
#
# #函数名可以赋值给变量，该变量为：函数对象
# my_sum=get_sum
# print(my_sum)
# print(my_sum(3,4))
#
# #闭包写法
# def fn_outer(num1):
#     #定义内部函数
#     def fn_inner(num2):#有嵌套
#         #求和
#         sum=num1+num2   #有引用
#         print(f"求和结果：{sum}")
#     return fn_inner  #有返回
#
# #调用上述函数
# fn_inner=fn_outer(10)
# fn_inner(1)#11
# fn_inner(1)#11
# fn_inner(1)#11
# fn_inner(20)#30
# print("_"*23)
#
# fn_outer(100)(200)#300

"""
nonlocal:Python内置的关键字，可以实现在内部函数中修改外部函数的变量值
"""

#内部函数访问外部函数的参数a=100
#定义外部函数
def fn_outer():
    #定义外部函数的（局部）变量
    a=100
    #定义内部函数，访问外部函数变量
    def fn_inner():
        #在内部函数中修改外部函数的变量
        nonlocal a      #nonlocal:内部函数中修改外部函数的变量值
        a=a+1
        #打印外部函数的变量
        print(f"a:{a}")

    #返回内部函数名（对象）
    return fn_inner

#测试
if __name__=="__main__":
    fn_inner=fn_outer()
    fn_inner()#101
    fn_inner()#102
    fn_inner()#103













"""
装饰器：本质闭包函数
    前提条件：有嵌套/有引用/有返回/额外功能

    用法:1.
        装饰后的函数名=装饰器名（被装饰的原函数名）
        装饰后的函数名（）
    用法2.
        在装饰的被原函数上，直接写@装饰器名，之后直接调用原函数
"""

# #定义外部函数，形参列表接收 要被装饰的函数名（对象）
# def check_login(fn_name):#fn_name:要被装饰的函数名（对象）
#     def fn_inner():     #有嵌套
#         #额外功能
#         print("校验登录...登录成功！")
#         #访问原函数，即外部函数的引用
#         fn_name         #有引用
#     #返回内部函数对象
#     return fn_inner     #有返回
# #定义内部函数，表示发表评论
# def comment():
#     print("发表评论")
#
# @check_login        #底层是: payment=check_login(payment)
# def payment():
#     print("充值中...")
#
# #测试
# #传统写法
# comment=check_login(comment)
# comment()
# print("-"*23)
#
# #语法糖
# payment()
#
#######无参无返回#######
# #定义装饰器
# def my_decorator(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner():             #有嵌套
#         #添加额外信息
#         print("正在计算中。。。")  #有额外功能
#         #调用原函数
#         fn_name()               #有引用
#     #返回内部函数（对象）
#     return fn_inner             #有返回
#
# #定义原函数
# @my_decorator
# def get_sum():
#     a=20
#     b=30
#     sum=a+b
#     print(f"求和结果为：{sum}")
#
# #测试
# #传统方式
# # get_sum=my_decorator(get_sum)
# # get_sum()
#
# #语法糖
# get_sum()

# #######有参无返回#######
# # 定义装饰器
# def my_decorator(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner(a,b):             #有嵌套
#         #添加额外信息
#         print("正在计算中。。。")  #有额外功能
#         #调用原函数
#         fn_name(a,b)               #有引用
#     #返回内部函数（对象）
#     return fn_inner            #有返回
#
# #定义原函数
# @my_decorator
# def get_sum(a,b):
#     sum=a+b
#     print(f"求和结果为：{sum}")
#
# #测试
# #传统方式
# # get_sum=my_decorator(get_sum)
# # get_sum()
#
# #语法糖
# get_sum(10,20)

# #######无参有返回#######
# # 定义装饰器
# def my_decorator(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner():             #有嵌套
#         #添加额外信息
#         print("正在计算中。。。")  #有额外功能
#         #调用原函数
#         return fn_name()               #有引用
#     #返回内部函数（对象）
#     return fn_inner            #有返回
#
# #定义原函数
# @my_decorator
# def get_sum():
#     a=10
#     b=20
#     return a + b
#
# #测试
# #传统方式
# # get_sum=my_decorator(get_sum) #本质：get_sum=fn_inner
# # sum=get_sum()
# # print(f"求和结果为：{sum}")
# #语法糖
# sum=get_sum()
# print(f"求和结果为：{sum}")

# #######有参有返回#######
# # 定义装饰器
# def my_decorator(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner(a,b):             #有嵌套
#         #添加额外信息
#         print("正在计算中。。。")  #有额外功能
#         #调用原函数
#         return fn_name(a,b)               #有引用
#     #返回内部函数（对象）
#     return fn_inner            #有返回
#
# #定义原函数
# @my_decorator
# def get_sum(a,b):
#     return a + b
#
# #测试
# #传统方式
# get_sum=my_decorator(get_sum) #本质：get_sum=fn_inner
# sum=get_sum(10,20)
# print(f"求和结果为：{sum}")
# #语法糖
# # sum=get_sum()
# # print(f"求和结果为：{sum}")

# #######可变参数#######
# # 定义装饰器
# def my_decorator(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner(*args,**kwargs):             #有嵌套
#         #添加额外信息
#         print("正在计算中。。。")               #有额外功能
#         #调用原函数
#         return fn_name(*args,**kwargs)               #有引用
#     #返回内部函数（对象）
#     return fn_inner                          #有返回
#
# #定义原函数
# @my_decorator
# def get_sum(*args,**kwargs):
#     """
#
#     :param args: 数字元组，接收所有位置参数，封装到元组
#     :param kwargs:接收所有关键字参数，封装到字典
#     :return:
#     """
#     #定义求和变量
#     sum=0
#     # 遍历元组，获取每个元素，求和
#     for i in args:
#         sum+=i
#     #遍历字典，获取每个值
#     for k,v in kwargs.values():
#         sum+=v
#     #返回结果
#     return sum
#     #上述代码可以优化为如下：
#     # return sum(args)+sum(kwargs.values())
#
# #测试
# #传统方式
# sum=get_sum(1,2,3,a=4,b=5,c=6)
# print(sum)

# #######多个装饰器装饰一个函数#######
# """
# 多个装饰器装饰一个函数，按照从内到外的顺序进行装饰（传统）从上到下（语法糖）
# """
# # 定义装饰器
# def check_login(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner():             #有嵌套
#         #添加额外信息
#         print("校验登录！。。。")               #有额外功能
#         #调用原函数
#         fn_name()               #有引用
#     #返回内部函数（对象）
#     return fn_inner         #有返回
#
# # 定义装饰器
# def check_code(fn_name):
#     #定义内部函数，格式与原函数保持一致
#     def fn_inner():             #有嵌套
#         #添加额外信息
#         print("校验验证码！。。。")               #有额外功能
#         #调用原函数
#         fn_name()               #有引用
#     #返回内部函数（对象）
#     return fn_inner         #有返回
#
# #定义原函数
# #语法糖:从上到下
# # @check_login
# # @check_code
# def comment():
#     print("发表评论！")
#
# #测试
# #传统方式:从内到外，可以理解为栈
# comment=check_code("comment")
# comment=check_login("comment")
# comment()



#######一个装饰器装饰多个函数(优化版)#######
"""
1.一个装饰器的参数有且只能有一个
2.如果装饰器有多个参数，可以在该装饰器的外边再包裹一层，把该装饰器当作其内部函数返回即可
"""
# 定义装饰器

def my_decorator(fn_name):# fn_name:原函数名。 flag:标记
    #定义内部函数，格式与原函数保持一致
    def fn_inner(a,b):             #有嵌套
        #添加额外功能
        if fn_name.__name__ =="get_sum":
            print("正在努力计算加法中...")
        elif fn_name.__name__ =="get_sub":
            print("正在努力计算减法中...")
        #调用原函数
        return fn_name(a,b)               #有引用
    #返回内部函数（对象）
    return fn_inner

#定义原函数
@my_decorator
def get_sum(a,b):
    return a+b

@my_decorator
def get_sub(a,b):
    return a-b

#测试
print(get_sum(10,20))
print("-"*23)
print(get_sub(35,15))

"""
深浅拷贝：
1.浅拷贝：copy模块的copy（），浅拷贝只拷贝对象本事
  深拷贝：copy模块的deepcopy()，深拷贝不仅拷贝对象，还拷贝对象相关的所有可变类型的引用
2.深拷贝拷贝的多，浅拷贝拷贝的少
3.深浅拷贝主要是针对可变类型来讲的，深拷贝拷贝所有层（可变），浅拷贝只拷贝第一层（可变）
若针对不可变类型，用法和普通赋值一样，无区别
"""

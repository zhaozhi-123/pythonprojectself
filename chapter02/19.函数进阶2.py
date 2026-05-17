# #函数的参数类型
# #加
# def add(x,y):
#     return x+y
# #减
# def subtract(x,y):
#     return x-y
# #乘
# def multiply(x,y):
#     return x*y
# #除
# def divide(x,y):
#     return x/y
#
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(2,3,add))
#

#匿名函数
#需求1：打印一个分割线
# def out_line():
#     print("----------")

# out_line=lambda : print("-------------")
# out_line()
#
# #需求2：两数相加
# # def add(x,y):
# #     return x+y
#
# add=lambda a,b: a+b
# print(add(1,2))
#

# 需求3：从小到大排序
# data_list=["C","C++","Python","PHP","Java","Go"]
# print(data_list)
#
# data_list.sort(key=lambda  item: len(item),reverse=True) #reverse=True 反转排序
# print(data_list)
# print(data_list)

#案例:计算n的阶乘
#递归调用
"""
jc(10)=10*jc(9)
jc(9)=9*jc(8)
jc(8)=8*jc(7)
jc(7)=7*jc(6)
jc(6)=6*jc(5)
jc(5)=5*jc(4)
jc(4)=4*jc(3)
jc(3)=3*jc(2)
jc(2)=2*jc(1)
jc(1)=1
"""

# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n*jc(n-1)
#
# result=jc(10)
# print(result)

"""
案例2：定义一个用于根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费计算订单总金额的函数
规则如下：
    1.优惠券要商品金额满1000才可以使用，优惠券金额不可超过商品总价
    2.积分需要商品总金额满500才可使用，100积分抵扣1元且抵扣不可超过商品总价
"""
def calc_order_cost(*args:tuple[str,float,int],coupon:int=0,score:int=0,express:float=0.0):
    """

    :param args: 商品信息，优惠信息 
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return:订单的总金额
    """
    #订单的总金额=商品总金额+运费-优惠券-积分抵扣
    #计算商品总金额
    total_price=[goods[1]*goods[2] for goods in args]
    total_cost=sum(total_price)


    #扣除优惠券
    if total_cost>=1000 and coupon<=total_cost:
        total_cost-=coupon

    #扣除积分抵扣部分
    if total_cost>=500 and score//100<=total_cost:
        total_cost-=score//100

    # 添加运费
    total_cost += express

    return total_cost

#测试用例
total_cost=calc_order_cost(("发夹",2,8),("键盘",58,1),("台灯",80,1),("抽纸",3,80),coupon=500,score=10000,express=9.9)
print(total_cost)

total_cost=calc_order_cost(("发夹",200,8),("键盘",388,1),("台灯",180,2),("手机",4888,1),coupon=500,score=10000,express=9.9)
print(total_cost)




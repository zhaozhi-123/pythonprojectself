#定义类
# class Car:
#     pass
#
#创建对象
# c1=Car()
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand="BMW"
# c1.name="X5"
# c1.price="500000"
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__)
#上述方法过于动态

#定义类
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name=c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕。 ")
#
# #创建对象
# c1=Car("红色","BMW","X7","800000")
# print(c1.__dict__)
#
# c2=Car("白色","奔驰","E300","450000")
# print(c2.__dict__)
#









#----------------定义类 实例方法-------------------
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = float(c_price)
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕.")
#
#     #定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶中...")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车的总费用，车价+税费
#         :param discount:折扣
#         :param rate:税率
#         :return:提车的总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
# #测试
# c1 = Car("红色", "BMW", "X7", "800000")
#
# #调用对象中的方法
# c1.running()
#
# total=c1.total_cost(0.9,0.1)
# print(f"提车的总费用为：",total)



#----------------实例属性与类属性-------------------
# class Car:
#     #类属性（所有实例对象共享）
#     wheel=4     #轮胎数量
#     tax_rate=0.1#购置税税率
#
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         #实例属性
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = float(c_price)
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕.")
#
#     def running(self):
#         print(f"{self.brand}{self.name}正在高速行驶中...")
#
#     def total_cost(self,discount,rate=0.1):
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
#
# #测试
# c1 = Car("红色", "BMW", "X7", "800000")
# print(c1.brand)
# print(c1.wheel)#通过实例对象查找时，先查找实例属性：实例属性不存在，再查找类属性
#
# #通过类名访问类属性
# print(Car.wheel)
# print(Car.tax_rate)
#
#
# c2 = Car("白色", "奔驰", "E500", "6000000")
# print(c2)
#
# print(c1==c2)
#
# print(c1<c2)
#

#----------------定义类 魔法方法-------------------
class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = float(c_price)
        print("Car类型的对象初始化完毕，对象属性已经添加完毕.")

    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中...")

    def total_cost(self,discount,rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost

    def __str__(self):
        return f"{self.color}{self.brand}{self.name}{self.price}"

    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


#测试
c1 = Car("红色", "BMW", "X7", "800000")
print(c1)

c2 = Car("白色", "奔驰", "E500", "6000000")
print(c2)


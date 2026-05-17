"""
property属性：
        把函数当做变量来使用
    实现方式：
        方式1：装饰器
        方式2：类属性
property的装饰器用法
    @property               修饰 获取值的函数
    @获取值的函数名.setter     修饰 设置值的函数

property类属性的用法：
    类属性名=property(获取值的函数名，设置值的函数名)

    可以直接 .上述函数名 来当作变量使用

"""

class Student:
    #私有属性
    def __init__(self):
        self.__age=20

    #公共的访问方式
    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

    #封装上述的公共方式为 类属性
    #参1：获取值的函数名     参2：设置值的函数名
    age=property(get_age,set_age)



if __name__ == '__main__':
    #创建对象
    s=Student()
    #设置值
    s.age=90
    #获取值
    print(s.age)


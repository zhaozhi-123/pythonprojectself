"""
property属性：
        把函数当做变量来使用
    实现方式：
        方式1：装饰器
        方式2：类属性
property的装饰器用法
    @property               修饰 获取值的函数
    @获取值的函数名.setter     修饰 设置值的函数

    可以直接 .上述函数名 来当作变量使用

"""

class Student:
    #私有属性
    def __init__(self):
        self.__age=18

        #提供公共访问方式
        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self,age):
            self.__age=age

if __name__ == '__main__':
    #创建对象
    s=Student()
    #设置值
    s.age=20
    #获取值
    print(s.age)


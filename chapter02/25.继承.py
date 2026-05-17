######### 继承入门 #########
# class Father(object):
#     def __init__(self):
#         self.gender = '男'
#
#     def walk(self):
#         print("饭后走一走，活到九十九")
#
# class Son(Father):
#     pass
#
# son= Son()
# print(f"性别：{son.gender}")
# son.walk()

######### 单继承 ###########
# class Master:
#     def __init__(self):
#         self.kongfu='古法配方'
#
#     def cake_make(self):
#         print(f"蛋糕制作采用{self.kongfu}摊饼")
#
# class student(Master): #单继承
#     pass
#
# p=student()
# p.cake_make()

######## 多继承 ###########
# class Master:
#     def __init__(self):
#         self.kongfu='古法配方'
#
#     def cake_make(self):
#         print(f"蛋糕制作采用{self.kongfu}摊饼")
#
# class School:
#         def __init__(self):
#             self.kongfu = 'AI配方'
#
#         def cake_make(self):
#             print(f"蛋糕制作采用{self.kongfu}摊饼")
#
#
# class Student(Master,School):
#     pass
#
# xm=Student()
# print(xm.kongfu)
# xm.cake_make()
#
# print(Student.mro()) #Stduent->Master->School->object #多继承原则：从左到右，就近原则

############# 子类重写父类 ##############
# class Master:
#     def __init__(self):
#         self.kongfu='古法配方'
#
#     def cake_make(self):
#         print(f"蛋糕制作采用{self.kongfu}摊饼")
#
# class School:
#         def __init__(self):
#             self.kongfu = 'AI配方'
#
#         def cake_make(self):
#             print(f"蛋糕制作采用{self.kongfu}摊饼")
#
#
# class Student(Master,School): #从左到右，就近原则
#     def __init__(self):       #重写父类
#         self.kongfu = '独创配方'
#
#     def cake_make(self):
#         print(f"蛋糕制作采用{self.kongfu}摊饼")
#
# xm=Student()
# print(xm.kongfu)
# xm.cake_make()

############ 子类访问父类 ##############
class Master:
    def __init__(self):
        self.kongfu='古法配方'

    def cake_make(self):
        print(f"蛋糕制作采用{self.kongfu}摊饼")

class School:
        def __init__(self):
            self.kongfu = 'AI配方'

        def cake_make(self):
            print(f"蛋糕制作采用{self.kongfu}摊饼")


class Student(Master,School): #从左到右，就近原则
    def __init__(self):
        self.kongfu = '独创配方'

    def cake_make(self):
        print(f"蛋糕制作采用{self.kongfu}摊饼")

    #方式一：父类名.父类函数名（self） ：精准访问

    def cake_make_master(self):
        Master.__init__(self)
        Master.cake_make(self)


    def cake_make_school(self):
        School.__init__(self)
        School.cake_make(self)

    # #方式二：super().父类函数名（）：只能访问最近父类，没有就往后查找
    # def make_old_cake(self):
    #     super().__init__()
    #     super().cake_make()

#多继承
# class Tusun(Student):
#     pass
#
# if __name__ == '__main__':
#     ts=Tusun()
#     ts.cake_make()          #Student类
#     ts.cake_make_master()   #Master类
#     ts.cake_make_school()   #School类

xm=Student()
print(xm.kongfu)
xm.cake_make()              #独创
# xm.cake_make_master()     #古法
# xm.cake_make_school()     #AI
xm.cake_make()              #与上一条相同
xm.make_old_cake()          #古法

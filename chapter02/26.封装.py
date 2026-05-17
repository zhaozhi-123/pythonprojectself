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
        #私有化
        self._money = 10000

    def cake_make(self):
        print(f"蛋糕制作采用{self.kongfu}摊饼")

    #方式一：父类名.父类函数名（self） ：精准访问

    def cake_make_master(self):
        Master.__init__(self)
        Master.cake_make(self)


    def cake_make_school(self):
        School.__init__(self)
        School.cake_make(self)

    def get_money(self):
        return self._money

class Tusun(Student):
    pass

if __name__ == '__main__':
    ts=Tusun()
    ts.cake_make()          #Student类
    ts.cake_make_master()   #Master类
    ts.cake_make_school()   #School类

    # print(ts._money())    #父类私有化，子类无法访问
    print(ts.get_money())   #通过父类提供的公共的访问方式，访问父类的私有成员
#########  多态  #########
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("狗叫：汪汪汪")
#
# class Cat(Animal):
#     def speak(self):
#         print("猫叫：喵喵喵")
#
#
# def make_noise(an):# an:Animal=Dog()      an：后不加Animal原因，只有警告，没用
#     an.speak()
#
# #测试
# if __name__ == '__main__':
#     # an:Animal = Dog()     #父类引用指向子类对象
#     # d:Dog = Dog()         #创建狗类对象
#
#     d=Dog()
#     c=Cat()
#
#     make_noise(d)
#     make_noise(c)

#案例：对象战斗平台
class HeroFighter:
    def power(self):
        return 60

class Adventurer(HeroFighter):
    def power(self):
        return 80

class EnemyFighter:
    def power(self):
        return 70

def object_play(hero,enemy):
    if hero.power()>enemy.power():
        print("英雄机 战胜 敌机")
    else:
        print("英雄机 惜败 敌机")

#测试
if __name__ == '__main__':
    h1 = HeroFighter()
    h2 = Adventurer()
    e1=EnemyFighter()

    #场景1
    object_play(h1,e1)
    print("_"*34)
    #场景2
    object_play(h2,e1)


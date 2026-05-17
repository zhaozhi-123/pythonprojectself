#定义抽象类
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass

#定义小米子类
class XiaoMi(AC):
    def cool_wind(self):
        print("小米 核心 制冷技术")

    def hot_wind(self):
        print("小米 核心 制热技术")

    def swing_l_r(self):
        print("小米 核心 静音左右摆风技术")

#定义格力子类
class Gree(AC):
    def cool_wind(self):
        print("格力 核心 制冷技术")

    def hot_wind(self):
        print("格力 核心 制热技术")

    def swing_l_r(self):
        print("格力 核心 静音左右摆风技术")

#测试
if __name__ == '__main__':
#小米测试
    xm=XiaoMi()
    xm.cool_wind()
    xm.hot_wind()
    xm.swing_l_r()
    print("-"*23)
#格力测试
    gl = Gree()
    gl.cool_wind()
    gl.hot_wind()
    gl.swing_l_r()


#该文件用于记录学生类，属性信息为：姓名，性别，年龄。手机号，描述信息

class Student:
    def __init__(self, name,gender, age,phone,desc):
        """
        该魔法方法用于初始化属性信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        return f"学生姓名：(self.name),性别：{self.gender},年龄：{self.age},手机号：{self.phone},描述信息：{self.desc}"

#测试
if __name__=="__main__":
    s=Student("乔","男",38,13234243678,"帮主")
    print(s)

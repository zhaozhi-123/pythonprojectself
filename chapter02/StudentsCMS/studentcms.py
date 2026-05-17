#完成学生管理系统的具体业务的操作，即增删改查，保存学生信息
import time
from re import search
from Tools.scripts.generate_token import update_file

#导包
from student import Student

#创建学生管理系统
class StudentCMS(object):
    #魔法方法init，初始化属性信息
    def __init__(self):
        #创建空列表，存储学生信息
        self.stu_list=[
            Student("张三","男","21",2456,"想你"),
            Student("李四","女","24",4521,"樱花"),
            Student("王五","男","27",2256,"故乡")
        ]

    #实现管理系统界面的打印
    #该方法没有使用self，可以定义为静态方法
    @staticmethod
    def show_view(self):
        print("*"*23)
        print("学生管理系统V2.0版本")
        print("\t1.添加学生信息")
        print("\t2.删除学生信息")
        print("\t3.修改学生信息")
        print("\t4.查询单个学生信息")
        print("\t5.查询所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print("*"*23)

    #实现添加学生功能
    def add_student(self):
        #输入学生信息，并接收
        name=input("请输入学生名字：")
        gender=input("请输入学生性别：")
        age=input("请输入学生年龄：")
        phone=input("请输入学生电话：")
        desc=input("请输入学生描述信息：")
        #把上述信息封装到列表中
        stu=Student(name,gender,age,phone,desc)
        #把学生对象添加到列表中
        self.stu_list.append(stu)
        #提示
        print(f"添加{name}学生信息成功！\n")


    #实现删除学生功能
    def del_student(self):
        del_name=input("请输入要删除的学生姓名：")
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f"学生{del_name}信息删除成功~\n")
                break
            else:
                print("查无此人，请重新检查!\n")
    #实现修改学生功能
    def update_student(self):
        # 根据学生姓名找到该学生的信息
        update_name=input("请输入要修改的学生姓名：")
        #遍历列表，找到要修改的学生，并修改
        for stu in self.stu_list:
            if stu.name == update_name:
                stu.name=input("请录入修改后的性别：")
                stu.age=input("请录入修改后的年龄：")
                stu.phone=input("请录入修改后的电话：")
                stu.desc=input("请录入修改后的描述信息：")

                print(f"学生{update_name}信息修改成功！：\n")
                break
            else:
                print("查无此人，请重新操作！\n")

    #实现查询单个学生功能
    def search_one_student(self):
        #提示用户输入要查找的学生姓名
        search_name=input("请输入要查找的学生姓名：")
        #遍历列表
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu,end="\n\n")
                break
            else:
                print("查无此人，请重新操作！")
    #实现查询所有学生功能
    def search_all_student(self):
        #判断长度是否为0
        if len(self.stu_list)==0:
            print("暂无学生信息，请先添加\n")
        else:
            #遍历列表，打印所有学生信息
            for stu in self.stu_list:
                print(stu)
            print()#为了格式好看，添加换行
    #实现保存学生信息功能
    def save_student(self):
        # #关联 学生信息文件
        # with open("./StudentsCMS/stu.txt","w",encoding="utf-8")as dest_f:
        #     #对象转为字典
        #     stu_dict=[stu.__dict__ for stu in self.stu_list]
        #     #字典列表持久化到文件中
        #     dest_f.write(str(stu_dict))#转为字符串再写入
        pass
    #
    #实现加载学生信息
    def load_student(self):
        #异常处理
        try:
        #关联学生信息文件
            with open("./StudentsCMS/stu.txt","w",encoding="utf-8") as src_f:
                #读取所有数据
                stu_data=src_f.read()
                #转为列表
                stu_list=eval(stu_data)
                #判断列表是否为空
                if len(stu_list)==0:
                    stu_list=[]
                #转为学生对象
                self.stu_list=[Student(**stu_dict) for stu_dict in stu_list]
        except:
            #目的地文件不存在，创建即可
            with open("./StudentsCMS/stu.txt", "w", encoding="utf-8") as src_f:
                pass

    #实现开始功能
    def start(self):
        #加载学生信息
        self.load_student()
        while True:
            #为了效果更明显，加入:延迟(休眠线程)
            time.sleep(1)
            #打印学生管理系统的界面
            StudentCMS.show_view()
            #提示用户录入编号，并接收
            #根据用户输入的编号，做不同的操作
            input_num=input("请输入要操作的编号：")
            if input_num=="1":
                # print("添加学生信息\n")
                self.add_student()
            elif input_num=="2":
                # print("删除学生信息\n")
                self.del_student()
            elif input_num=="3":
                # print("修改学生信息\n")
                self.update_student()
            elif input_num=="4":
                print("查询单个学生信息\n")
                self.search_one_student()
            elif input_num=="5":
                print("查询所有学生信息\n")
                self.search_all_student()
            elif input_num=="6":
                self.save_student()
                print("保存学生信息成功！\n")

            elif input_num=="0":
                result=input("您确定要退出吗？（Y/N）->")
                if result.lower()=="y":#把字母转成小写
                    #退出前自动保存
                    self.save_student()
                    print("谢谢您的使用，期待下次再会\n")
                    break
            else:#输入错误
                print("输入错误\n")
#在main中测试
if __name__=="__main__":
    cms=StudentCMS()
    cms.start()



from StudentsCMS.student import Student

#需求：把学生对象->字典形式，属性名做键，属性值做值
s1=Student("张三","男","21",2456,"想你")
my_dict_=s1.__dict__
print(my_dict_)
print(type(my_dict_))
print("_"*23)

#需求：把[学生对象,学生对象,学生对象]->[字典，字典，字典]

s1=Student("张三", "男", "21", 2456, "想你")
s2=Student("李四", "女", "24", 4521, "樱花")
s3=Student("王五", "男", "27", 2256, "故乡")
stu_list=[s1,s2,s3]

#
list_dict=[]
# for stu in stu_list:
#     list_dict.append(stu.__dict__)
# print(list_dict)
#列表推导式
list_dict=[stu.__dict__ for stu in stu_list]
print(list_dict)
print("_"*23)

#字典转为学生对象
my_dict_= {'name': '张三', 'gender': '男', 'age': '21', 'phone': 2456, 'desc': '想你'}
s5=Student(**my_dict_)
print(type(s5))


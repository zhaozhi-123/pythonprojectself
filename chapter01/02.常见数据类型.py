#常见数据类型 type()获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))#str
# print(type(10))#int
# print(type(3.14))#float
# print(type(True))#bool
# print(type(False))#bool
# print(type(None))#NoneType

# num=-100
# print(type(num))#int

#常见数据类型 isinstance(数据，类型) bool值-判定数据是否指定类型
# print(isinstance(num,int))#True
# print(isinstance(num,float))#Flase
# print(isinstance(num,bool))#Flase

#字符串
# 定义字符串的三种方式
# s1="Hello"#双引号定义
# s2='Python'#单引号定义
# s3="""
# Hello:
# 欢迎大家进入Python课程的学习！
# 大家记得一键三连哦~
# """
#三引号定义（多行字符串）

# print(s1)
# print(s2)
# print(s3)

# #定义字符串 "It's very good"
# #转义字符\' \" \n \t
# msg='It\'s very good'
# print(msg)

# msg2="It's very good"
# print(msg2)

# msg3= "Hello 的意思就是 \"您好\""
# print(msg3)

# msg4= 'Hello 的意思就是 \"您好\"'
# print(msg4)
# #\n 换行  \t按Tab缩进

#字符串拼接
# s1="人生苦短" "我用Python" "，OK"
# print(s1)

# msg1="人生苦短"
# msg2="我用Python"
# print("叔说:"+msg1+","+msg2)

#案例 加号（+）只能拼接字符串     str(int数字)-int类型变为str类型
# name="涛哥"
# age=18
# pro="软件工程"
# hobby="Python,Java"
# print("大家好，我是"+name+",今年"+str(age)+"岁，学习的专业是"+pro+"爱好是"+hobby)

#案例 字符串格式化 占位符%s
# name="涛哥"
# age=18
# pro="软件工程"
# hobby="Python,Java"
# print("大家好，我是%s,今年%s岁，学习的专业是%s爱好是%s"%(name,age,pro,hobby))

#案例 字符串格式化
name="涛哥"
age=18
pro="软件工程"
hobby="Python,Java"
print(f"大家好，我是{name},今年{age}岁，学习的专业是{pro}爱好是{hobby}") #f"..{变量名/表达式}..


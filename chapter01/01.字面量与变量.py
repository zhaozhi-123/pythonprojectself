# 字面量的写法
# print(100)#整数int
# print(3.14)#浮点数float
# print(True)#布尔bool
# print(False)#布尔bool
# print("Hello World")#字符串str
# print("------------")#字符串str
# print(None)#空值NoneType
#
# print(True+1)#True-1 False-0 布尔类型本质也是整数

#变量 Python为动态类型语言
# num=1114.1
# print(num)
#
# num=num+1
# print(num)
#
# num="ok"
# print(num)
#
# num=True
# print(num)
#
# a=True
# print(a)

#案例
# base,incr=20.7,50
# print("未来第一个月的播放量：",base+incr)
# print("未来第二个月的播放量：",base+incr+incr)

#案例1：交换a，b两变量的值
# a=10
# b=20
#
# c=a#c=10
# a=b#a=20
# b=c#b=10
#
# print(a,b)

#练习1：交换a,b,c三变量的值
a=100
b=200
c=300

d=a
a=b
b=c
c=d

print(a,b,c)
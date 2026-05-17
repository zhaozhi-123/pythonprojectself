#算术运算符
# print("10+4=",10+4)#加
# print("10-4=",10-4)#减
# print("10*4=",10*4)#乘
# print("10/4=",10/4)#除 2.5
# print("10//4=",10//4)#除 2
# print("10%4=",10%4)#取余 2
# print("10**4=",10**4)#幂指数 10000
from operator import and_

#算术运算符优先级  ** -->  * / // % --> + - 先乘除再加减

#输入两个输 x 和 y，计算X+Y 和X-Y的结果
#float(..)转为浮点数
# x=float(input("请输入x的值"))
# y=float(input("请输入y的值"))
#
# print("x+y=",x+y)
# print("x-y=",x-y)

#赋值运算符
# num=85
#
# num+=10 #num=num+10  95
# print("num+=10后，num= ",num)
#
# num-=10 #num=num-10  85
# print("num-=10后，num= ",num)
#
# num*=10 #num=num*10  850
# print("num*=10后，num= ",num)
#
# num/=10 #num=num/10  85.0
# print("num/=10后，num= ",num)
#
# num//=10 #num=num//10  8.0 取整
# print("num/=10后，num= ",num)
#
# num%=3 #num=num%3  2.0 取余
# print("num/=10后，num= ",num)
#
#
# num**=3 #num=num**3 8.0
# print("num**=3后，num= ",num)

#比较运算符
# print("100==100吗:",100==100)#T
# print("'100==100'吗:","100==100")#T
# print("100 !=100 吗:", 100 !=100)#F
#
# print("100<100吗:",100<100)#F
# print("100<=100吗:",100<=100)#T
#
# print("100>100吗：",100>100)#F
# print("100>=100吗：",100>=100)#T

#逻辑运算符

#案例1：键盘输入一个整数，判定数字是否在10-20之间
# n=int(input("请输入一个整数："))
# print(f"{n}在10-20之间：", n>=10 and n<=20)
# print(f"{n}在10-20之间：", 10 <= n <= 20)

#案例2：键盘输入一个整数，判定数字是否不在10-20之间
n=int(input("请输入一个整数："))
print(f"{n}在10-20之间：", n<10 or n>20)
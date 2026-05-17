#for循环

# msg=input("请输入需要遍历的字符串：")
#
# for s in msg: #s表示遍历出来的元素；msg表示需要遍历的数据
#     print(f"元素：{s}")
# else:
#     print("遍历结束！")

#案例1；计算1-100之间的所以奇数之和
# total=0
#
# for i in range(1,101):
#     if i%2==1:#奇数
#         total+=i
# print("1-100之间的奇数累加之和为：",total)

#简化
# total=0
#
# for i in range(1,101,2):
#     total+=i
# print("1-100之间的奇数累加之和为：",total)

#计算100-500之间所有3的倍数的数字之和
# total=0
#
# for i in range(100,501):
#     if i%3==0:#i是三的倍数
#         total+=i
#
# print("1-100之间的倍数为3的数字累加之和为：",total)


#循环嵌套 print自带换行效果
# print("*",end=""):end表示每一次输出以什么结束；默认\n表示换行
#接受键盘录入m,n
# m=int(input("请输入长方形的长度："))
# n=int(input("请输入长方形的宽度："))
#
# for i in range(m):#控制行
#     for j in range(n):#控制列
#         print("*",end=" ")
#     print()#换行

#打印99乘法表
for i in range(1,10):# 外层循环控制行
    for j in range(1,i+1):  # 内层循环控制列
        print(f"{j} * {i} = {j*i}",end="\t")# \t  制表符
    print()






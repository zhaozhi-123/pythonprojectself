#列表操作
#定义列表-list
# s=[56,90,88,65,90,"A","Hello",True]
#
# print(type(s))
#
# #访问列表元素
# #获取
# print(s[0])#正向索引,从0开始
# print(s[-8])#反向索引，从-1开始
# print(s[2])
# print(s[-6])
#
# #修改
# s[5]="ABC"
# print(s)
#
# #删除
# del s[6]
# print(s)
#
# #遍历
# for item in s:
#     print(item)

#切片操作s[开始索引：结束索引：步长]
# s=["A","C","H","K","L","B","D","E"]

# print(s[0:5:1]) #默认[0:x:1],默认值可省略
# print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
# print(s[0:-2:1])

#列表定义
# s=[56,90,75,45,37,27,36,75,38,48,90]
# print(s)
#
# #append():在列表尾部追加元素
# s.append(188)
# print(s)
#
# #insert():在指定索引之前，插入元素
# s.insert(2,80)
# print(s)
#
# #remove():移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
#
# #pop():移除列表中指定索引位置的元素并返回
# e=s.pop(1)
# print(e)
#
# e=s.pop() #默认最后一个
# print(e)
#
# print(s)
#
# #sort排序
# s.sort()
# print(s)
#
# #reverse():反转列表元素
# s.reverse()
# print(s)

# #用户输入10个数字，存储在列表中，列表中数字排序，输出最小值，最大值和平均值
# #定义列表
# num_list=[]
#
# #用户输入的10个数字存入列表
# for i in range(10):
#     num=int(input("请输入一个有效的数字:"))
#     num_list.append(num)
#
# print("数字列表：",num_list)
#
# #排序
# num_list.sort()
#
# print("排序后的数字列表：",num_list)
#
# #输出其中的最小值，最大值和平均值 sum（）:求和 len（）:获取元素个数
# print("最小值:",num_list[0])
# print("最小值",min(num_list))
# print("最大值:",num_list[-1])
# print("最大值",max(num_list))
# print("平均值:",sum(num_list)/len(num_list))
#

#案例2：合并两列表，并去除重复元素

num_list1=[12,23,42,63,34,35,25,46,25,26,27]
num_list2=[23,45,15,76,45,32,45,15,26,27,16,36]
#合并列表

#初始
#1
# for num in num_list2:
#     num_list1.append(num)

#解包：将列表这一类容器解开成一个一个独立的元素
#组包：将多个值合并到一个容器
#2
# new_list=[*num_list1,*num_list2]

#直接加
#3
# new_list=num_list1+num_list2

# print("合并后的原始列表：",num_list1)
#
# #去除重复记录
# new_list=[] #去除重复记录后的列表
# for num in num_list1:
#     #判断nwe_list中是否存在num元素
#     if num not in num_list:#判断元素是否存在于列表中，存在为True
#         new_list.append(num)
#
# print("去除重复记录后的列表",new_list)

#案例：生成1-20的平方列表
#方式1：
# num_list=[]
# for i in range(1,21):
#     num_list.append(i**2)
#
# print(num_list)

#方式2：列表推导式：[要插入的值 for i in 序列/列表]/[要插入的值 for i in 序列/列表 if 条件]
# num_list2=[ i**2 for i in range(1,21)]
# print(num_list2)

#案例：从一个数字列表中提取所有偶数，计算其平方，组成一个新的列表
num_list=[23,24,14,35,12,53,63,25,15,11]
new_list=[i**2 for i in num_list if i%2==0]

print(new_list)


#元组基本操作-tuple
# #定义
# t1=(80,95,78,50,76,80,85,20)
#
# print(t1)
# print(type(t1))
#
# #索引访问
# print(t1[0])
# print(t1[-1])
#
# #切片
# print(t1[0:5:1])
#
# #count()统计元素个数
# print(t1.count(80))
#
# #index()获取元素的索引（第一个元素的位置）
# print(t1.index(80))
#
# #注意点
# t2=()
# print(t2)
# print(type(t2))
#
# t3=(100,) #单元素元组需加",",否则为int类型
# print(t3)
# print(type(t3))

# #组包操作
# t1=(5,7,8,10,2,23,14)
# t2=5,7,8,10,2,23,14
#
# print(t1)
# print(t2)
#
# #解包操作 (*收集剩余元素，封装列表list中)
# a,b,c,d,e,f,g=t1
# print(a,b,c,d,e,f,g)
#
# first,second,*other,last=t1
# print(first,second)
# print(other)
# print(last)
#
# *other,last2,last1=t1
# print(other)
# print(last2)
# print(last1)
#
# #交换两个变量值，输出到控制台
# a=10
# b=20

# #解包
# t=b,a
# #组包
# a,b=t

# a,b=b,a
#
# print(a)
# print(b)
#
# #交换三变量输出到控制台 a=100,b=200,c=300,a,b,c=c,a,b,输出到控制台
# a=100
# b=200
# c=300
#
# c,a,b=a,b,c
#
# print(a)
# print(b)
# print(c)

"""
    根据学生成绩单完成下述需求
    1.计算每个学生的总分，各科平均分
    2.统计每科成绩的最低分，最高分，平均分
    3.查找成绩优秀的学生（平均分大于90）
"""
students=(
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",72,98,65),
    ("S004","李牛",72,68,75),
    ("S005","周衣",52,81,92),
    ("S006","王卓",91,84,93),
    ("S007","徐立军",92,48,15),
    ("S008","许木",22,48,85),
    ("S009","红蛇",26,78,92),
    ("S010","杨建国",91,81,93)
)


#计算总分，平均分 {avg:.1f}保留一位小数，以float类型
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]}\t {s[1]}\t {s[2]}\t\t {s[3]}\t\t{s[4]}\t\t{total}\t {avg:.1f}")

#统计各科目的最低分，最高分，平均分
chinese_scores=[s[2] for s in students]
math_scores=[s[3] for s in students]
english_scores=[s[4] for s in students]

print(f"语文最低分:{min(chinese_scores)}, 最高分:{max(chinese_scores)},平均分:{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)}, 最高分:{max(math_scores)},平均分:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(english_scores)}, 最高分:{max(english_scores)},平均分:{sum(english_scores)/len(chinese_scores)}")

#查找平均分大于90的学生
#方式一：
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     if avg>90:
#         print(f"学号:{s[0]},姓名:{s[1]},平均分:{avg:.1f}")

#方式二：
for id,name,chinese_scores,math_scores,english_scores in students:
    total=chinese_scores+math_scores+english_scores
    avg=total/3
    if avg>90:
        print(f"学号:{id},姓名:{name},平均分:{avg:.1f}")




#集合set定义-->无序，不可重复，可修改
s1={5,3,2,2,4,14,25,36,5,3}

print(s1)
print(type(s1))

s2=set()
print(s2)
print(type(s2))

#常见方法：
#add():添夹元素到集合
s1={100,200,300,400,500,600,700,800,900}
print(s1)

s1.add(1200)
print(s1)

#remove():移除集合中指定元素
s1.remove(200)
print(s1)

#pop():移除集合中指定元素并返回
e=s1.pop()
print(e)
print(s1)

#clear():清空集合
s1.clear()
print(s1)

s2={"A","B","C","D","E","X","Y"}
s3={"C","E","Y","Z"}

#difference():求差集（存在于第一个集合，不存在于第二个集合）
print(s2.difference(s3))
print(s3.difference(s3))

#union():求并集
print(s2.union(s3))

#intersection():求交集
print(s2.intersection(s3))


#集合set案例

#选修足球学生名单
football_set ={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set={"张铁","忠居仁","干林","美老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set ={"木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
#选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#同时选修法语和艺术的学生
#方式一：
fa_set=french_set.intersection(art_set)
print(f"同时选修了法语 和艺术的学生： {fa_set}")

#方式二：
fa_set2=french_set & art_set
print(f"同时选修了法语 和艺术的学生： {fa_set2}")

#同时选修四门课程的学生
all_set=football_set&basketball_set&french_set&art_set
print(f"同时选修了所有四门课程的学生：{all_set}")

#选修足球，没有选修篮球的学生
#方式一：
fb_set=french_set.difference(basketball_set)
print(f"选修足球，没有选修篮球的学生：{fb_set}")

#方式二：差集
fb_set2=french_set-basketball_set
print(f"选修足球，没有选修篮球的学生：{fb_set2}")

#方式三：{for s in set1}
fb_set3= {s for s in football_set if s  not in basketball_set}
print(f"选修足球，没有选修篮球的学生：{fb_set3}")

#统计每一个学生选修的课程数量
#获取学生名单--并集（|）
#方法一：
all_set=football_set.union(basketball_set).union(art_set).union(french_set)
print(all_set)

#方法二：
all_set2=football_set|basketball_set|art_set|french_set
print(all_set2)

#获取每一个学生选修的课程名单
all_list=[*football_set,*basketball_set,*art_set,*french_set]

for s in all_list:
    print(f"{s}选修了{all_list.count(s)}课程")
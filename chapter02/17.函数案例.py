# #案例1：定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高/2）
# def triangle_area(b,h):
#     """
#     根据传入的底和高计算三角形的面积
#     :param b:
#     :param h:
#     :return:
#     """
#     return b*h/2
# tr=triangle_area(20,10)
# print("三角形面积为：",tr)
#
# #案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s:
#     :param s:
#     :return:
#     """
#     num=0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num+=1
#     return num
#
# print("元音字母个数为：",count_aeiou('Hello Python'))
#
#
# #案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分，最低分，平均分（一位小数），返回值
# def  calc_score(score_list):
#     """
#     计算平均分，最高分，最低分,保留一位小数
#     :param score_list:
#     :return:平均分，最高分，最低分
#     """
#     max_s=max(score_list)
#     min_s=min(score_list)
#     avg_s=round(sum(score_list)/len(score_list),1)
#     return max_s,min_s,avg_s
#
# s_list=[342,325,356,567,357,467,452,235,468,642]
# max_s,min_s,avg_s=calc_score(s_list)
# print("最高分：",max_s)
# print("最低分：",min_s)
# print("平均分：",avg_s)

# """
# 需求1：定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90：A
# - 分数 >= 75：B
# - 分数 >= 60：C
# - 分数 < 60：D
# """

# def get_grade(grade):
#     if grade >= 90:
#         return 'A'
#     elif grade >= 75:
#         return 'B'
#     elif grade >= 60:
#         return 'C'
#     else :
#         return 'D'
# grade = float(input("请输入分数："))
#
# print("分数等级为：",get_grade(grade))

# """
# 需求2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
# """
#
# # 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome("level"))
# print(is_palindrome("hello"))
# print(is_palindrome("黄山落叶松叶落山黄"))
# print(is_palindrome("12321"))
# print(is_palindrome("12345"))

# """
# 需求3：定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# """
# # 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time_convert(seconds):
#     original_seconds = seconds
#     hours = seconds // 3600             # //整除
#     minutes = (seconds % 3600) // 60    # %取模
#     seconds = (seconds % 3600) % 60
#     return f"{original_seconds} 转换为 {hours} 小时 {minutes} 分钟 {seconds} 秒"
#
# print(time_convert(3773))
# seconds=int(input("请输入要转化的秒数"))
# print("秒数可以转化为：",time_convert(seconds))

"""
需求4：定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
"""
# 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
# def triangle_type(a, b, c):
#     if a+b>c and b+c>a and a+c>b:
#         if a==b==c:
#             return "等边三角形"
#         elif a==b or a==c or b==c:
#             return "等腰三角形"
#         else:
#             return "普通三角形"
#     else:
#         return "不能构成三角形"
#
# a=int(input("请输入三角形的第一条边长"))
# b=int(input("请输入三角形的第二条边长"))
# c=int(input("请输入三角形的第三条边长"))
# print("该三角形类型为：",triangle_type(a,b,c))





# #字符串 基本操作 (不可变化-无法修改)(有序性)（可迭代性）
# s = "Hello-Python"
#
# print(s[4])#正向索引 0开始
# print(s[-8])#反向索引 -1开始
#
# for i in s:
#     print(i)
#
# #切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1])
#
# print("--------------")
#
# #步长 ：->正数：从前往后截取 ； 负数：从后往前截取
# print(s[-1:-7:-1])
# print(s[::-1])
#
# #字符串常用方法
# s ="   Hello-Python-Hello-World   "
#
# #find() 查找指定字符串第一次出现的索引位置
# index=s.find("-")
# print(index)
#
# #count()统计子字符串在指定字符串中出现的次数
# c=s.count("o")
# print(c)
#
# #upper()转为大写
# su=s.upper()
# print(su)
#
# #lower()转为小写
# sl=s.lower()
# print(sl)
#
# #split 将字符串按照指定字符串切割-列表
# slist=s.split("-")
# print(slist)
#
# #strip() 去除字符串两端的空格
# ss=s.split()
# print(ss)
#
# #replace() 将字符串中的指定子串替换为新内容
# sr=s.replace("-","_")
# print(sr)
#
# #startswith()/endswith()判断字符串是否是以指定的字符串开头/结尾，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))

# #邮箱格式验证（至少一个@，一个.）
# #方式一:
# # #接收用户输入的邮箱
# mail=input("请输入邮箱：")
#
# #判断邮箱格式
# if mail.count("@")==1 and mail.count(".")>=1:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")
#
# #方式二： in运算符--> 判断子串是否存在字符串中，存在，返回True：
# #接收用户输入的邮箱
# mail=input("请输入邮箱：")
#
# #判断邮箱格式
# if mail.count("@")==1 and "."in mail:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")
#


# 1. 输入一个字符串, 判断该字符串是否是回文(两边对称) 。  "黄山落叶松叶落山黄"  "上海自来水来自海上"
s = input("请输入一个字符串: ")

# 方式一(双指针法): 思路是从两边向中间遍历, 基于索引获取两边字符对比, 如果两边的字符不相等, 则不是回文, 否则是回文。

left = 0 # 左索引
right = len(s) - 1 # 右索引
flag = True

while left < right:
    if s[left] != s[right]:
        flag = False
        break
    left += 1 #左指针右移
    right -= 1 #右指针左移

if flag:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")


# 方式二:
if s == s[::-1]:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")

# 2. 将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。
s_list = []

for i in range(10):
    s = input("请输入一个字符串: ")
    s_list.append(s[::-1].upper())
print("输入的字符串列表为:", s_list)

print("--------------------------------")

print("反转后的字符串列表为:")
for s in s_list:
    print(s)
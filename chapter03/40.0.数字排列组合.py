"""
需求：1，2，3，4能组成的四位数有几种情况，按照五个一行输出

1. 5个一行输出
2. 包含1，2，3，4这四个数字
3. 要求1和3不能挨着
4. 数字4不能开头
5. 五行之内
"""

#数字->字符串，调用字符串功能做判断

# count=0
# for s in [str(i) for i in range(1234,4322)]:  #左边包含，右边不包含
#     if "1"in s and "2"in s and "3"in s and "4"in s and "13" not in s and "31" not in s and s[0]!="4":
#         count+=1
#         print(s,end="\n" if count%5==0 else "\t")

#需求：已知列表：my_list=["aa","bb","cc","bb","bb","bb","dd"],删除所有bb元素
#思路1：
# my_list=["aa","bb","cc","bb","bb","bb","dd"]
# new_list=[s for s in my_list if s!="bb"]
# print(new_list)

#思路2：
my_list=["aa","bb","cc","bb","bb","bb","dd"]
for s in my_list[:]:    #切片
    if s == "bb":
        my_list.remove(s)
print(my_list)




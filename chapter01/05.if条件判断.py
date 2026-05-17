#if条件判断
# score=700
# if score>680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
# print("-------------------------")

#案例：输入账号和密码实现登录功能
# ok_account="188888888"
# ok_password="666888"
# #1.接受用户输入的账号和密码
# account=input("请输入您的账号：")
# password=input("请输入您的密码：")
#
# #2.判断账号和密码是否全部正确，都正确，登录成功
# if account==ok_account and password==ok_password:
#     print("登录成功")
#     print("进入首页")
# #判断账号和密码是否有错误的，若有，则登失败，提示错误信息
# if account!=ok_account or password!=ok_password:
#     print("登录失败！")
#     print("账号或密码错误！")

    # 案例：输入账号和密码实现登录功能
    # ok_account = "188888888"
    # ok_password = "666888"
    # # 1.接受用户输入的账号和密码
    # account = input("请输入您的账号：")
    # password = input("请输入您的密码：")
    #
    # # 2.判断账号和密码是否全部正确，都正确，登录成功
    # if account == ok_account and password == ok_password:
    #     print("登录成功")
    #     print("进入首页")
    # else:
    #     print("登录失败！")
    #     print("账号或密码错误！")

#案例：根据用户输入的年分，判断闰年
# year=int(input("请输入需要判定的年份:"))
#
# if (year%100!=0 and year%4==0) or (year%400==0 ):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

#案例：根据用户输入的数字，判断数字是奇数还是偶数
# num=int(input("请输入一个数字"))
# if(num%2==0):
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

#案例：根据用户输入年龄，判断是否成年
# age=int(input("请输入年龄"))
# if(age>=18):
#     print("您已经成年")
# else:
#     print("您还未成年")

#案例：根据用户输入数字，判断该数字是正数，负数还是0
# num=int(input("请输入数字："))
# if num>0:
#     print(f"{num}是正数")
# elif num<0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

#案例：根据输入的用户名和密码进行登录 admin/666888    root/547527    zhangsan/123456
# username=input("请输入用户名：")
# password=input("请输入密码：")
#
# if username=="admin" and password=="666888":
#     print("登录成功1")
# elif username=="root" and password=="547527":
#     print("登陆成功2")
# elif username=="zhangsan" and password=="123456":
#     print("登陆成功3")
# else:
#     print("登陆失败，用户名或密码错误")

#案例：根据输入的考试成绩，判断成绩等级
# score = int(input("请输入考试分数: "))
# if score >= 85:
#     print(f"{score} 分, 优秀")
# elif score >= 60:
#     print(f"{score} 分, 及格")
# else:
#     print(f"{score} 分, 不及格")

#案例：根据输入的购物车的商品总额，及折扣规则计算应付金额

# total_price = float(input("请输入购物车商品总额: "))
#
# if total_price >= 500:
#     print(f"{total_price} 元商品, 8折, 实际应付: {total_price * 0.8} 元")
# elif total_price >= 300:
#     print(f"{total_price} 元商品, 9折, 实际应付: {total_price * 0.9} 元")
# elif total_price >= 100:
#     print(f"{total_price} 元商品, 95折, 实际应付: {total_price * 0.95} 元")
# else:
#     print(f"{total_price} 元商品, 无折扣, 需支付: {total_price} 元")

#案例：三角形类型判断   pass 空语句，语法占位
# a=int(input("请输入第一个边的边长"))
# b=int(input("请输入第二个边的边长"))
# c=int(input("请输入第三个边的边长"))
#
# if a+b>c and a+c>b and b+c>a:
#     if a==b and b==c:
#         print(f"{a}{b}{c}这三个边长构成等边三角形！！！")
#     elif a==b or b==c or a==c:
#         print(f"{a}{b}{c}这三个边长构成等腰三角形！！！")
#     else:
#         print(f"{a}{b}{c}这三个边长构成普通三角形！！！")
# else:
#     print(f"{a}{b}{c}这三个边长不能构成三角形！！！")

#案例：阶梯电价
usage_electricity=int(input("请输入用电量:"))

#定义价格
first_max=2880
second_max=4800

first_price=0.4883
second_price=0.5383
third_price=0.7883

total_cost=0.0
#第一阶梯
if usage_electricity<=first_max:
    total_cost=first_price*usage_electricity
#第二阶梯
elif usage_electricity<=second_max:
    #第一档
    first_cost=first_price*first_max
    #第二档
    second_usage=usage_electricity-first_max
    second_cost=second_price*second_usage

    total_cost=first_cost+second_cost

#第三阶段
else:
#第一档
    first_cost=first_price*first_max
#第二档
    second_usage=second_max-first_max
    second_cost=second_price*second_usage
#第三档
    third_usage=usage_electricity-second_max
    third_cost=third_price*third_usage
    total_cost=first_cost+second_cost+third_cost

print(f"{usage_electricity}度的电费是:{total_cost}元")



















#案例：根据输入的用户名和密码进行登录 admin/666888    root/547527    zhangsan/123456
#条件判断用while
#break:用于循环，表示结束，跳出循环
#continue:用于循环，中断本次循环，进入下次循环
# while True:
#     #接收输入的用户数据
#     username=input("请输入用户名：")
#     password=input("请输入密码：")
#     #校验用户数据
#     if username=="" and password=="":
#         print("输入的用户名和密码不能为空！")
#         continue#结束当前循环，进入下一轮循环
#
#     #判断用户数据是否匹配
#     if username=="admin" and password=="666888":
#         print("登录成功1")
#         break #跳出循环
#     elif username=="root" and password=="547527":
#         print("登陆成功2")
#         break
#     elif username=="zhangsan" and password=="123456":
#         print("登陆成功3")
#         break
#     else:
#         print("登陆失败，用户名或密码错误")

for i in range(5):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if username == "" and password == "":
        print("输入的用户名和密码不能为空！")
        continue#结束当前循环，进入下一轮循环

    if username == "admin" and password == "666888":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "123456 ":
        print("登录成功")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功")
        break
    else:
        print("登录失败")
        if i == 4:
            print("输入错误五次，不允许再登录")
            break
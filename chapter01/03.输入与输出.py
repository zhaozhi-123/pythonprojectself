#获取键盘上输入的数据 input(...)
# name=input("请输入您的姓名:")
# age=input("请输入您的年龄:")
#
# print(f"您的姓名是{name},年龄为:{age}")

#案例：银行卡ATM取款
#总金额
total=10000
#输入密码
password=input("请输入您的银行卡密码：")
print(f"密码正确，{password}")
#输入取款金额
num=input("请输入您的取款金额:")
#计算余额并输出 num转为int类型
print(f"取款后银行卡余额为{total-int(num)}")

#案例：计算输入两数和，并输出

#用户输入数字num1和num2
num1=input("请输入第一个数字")
num2=input("请输入第二个数字")
print(f"输入的第一个数字为{num1},输入的第二个数字为{num2}")
#计算两数和
print(f"两个数字之和为{int(num1)+int(num2)}")
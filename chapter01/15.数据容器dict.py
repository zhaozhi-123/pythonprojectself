#字典--{key:value}   key不可重复（若重复，覆盖前值）
#定义字典
# dict1={"王林":670,"李幕婉":608,"徐立国":588,"韩立":688}
#
# print(dict1)
# print(type(dict1))
#
# #key不可以是list,set,dict
# dict2={0:670,1.5:608,2:502,('A','B'):682}
# print(dict2)
# print(type(dict2))
#
# #访问
# print(dict1["李幕婉"]) #获取
# dict1["李幕婉"]=688 #修改
# print(dict1)

# #常见操作
# dict1 = {"王林": 670, "李幕婉": 608, "许立国": 588, "韩立": 688}
# print(dict1)
#
# #添加
# dict1["涛哥"]=550
# print(dict1)
#
# #修改
# dict1["涛哥"]=620
# print(dict1)
#
# #查询
# #根据key获取value
# print(dict1["涛哥"])
# print(dict1.get("涛哥"))
#
# print(dict1.keys())#获取所有的key
# print(dict1.values())#获取所有的value
# print(dict1.items())#获取所有的键值对 key:value
#
# #删除
# score=dict1.pop("许立国") #pop-删除并返回值 score为返回值
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}：:{dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")
#
# for k,v in dict1.items(): #解包
#     print(f"{k}:{v}")


# #案例：购物车
# shopping_cart={}
# menu="""
# ########购物车系统########
# #     1.添加购物车       #
# #     2.修改购物车       #
# #     3.删除购物车       #
# #     4.查询购物车       #
# #     5.退出购物车       #
# ########################
# """
# print(shopping_cart)
# print(shopping_cart.keys())
#
# #制作菜单 ---alt+shift 列编辑

# print("欢迎使用购物车管理系统~")
# while True:
#
#     print(menu)
#
# #执行的具体操作
#     choice=input("请选择要执行的操作（1-5）:")
#     match choice:
#         case "1":#添加购物车
#             goods_name=input("请输入商品名称")
#             goods_price = float(input("请输入商品价格"))
#             goods_num = int(input("请输入商品数量"))
#
#             #判断商品是否存在
#             if goods_name in shopping_cart:
#                 print("该商品已存在，请重新选择")
#             else:
#                 shopping_cart[goods_name]= {"price":goods_price,"num":goods_num}
#                 print("商品添加完毕")
#         case "2":#修改购物车
#             goods_name = input("请输入修改后的商品名称")
#             if goods_num not in shopping_cart:
#                 print("该商品不存在，请重新选择")
#                 continue#进行下次循环
#
#             goods_price = float(input("请输入商品最新价格"))
#             goods_num = int(input("请输入商品最新数量"))
#             shopping_cart[goods_name]= {"price":goods_price,"num":goods_num}
#             print("商品修改完毕")
#
#         case "3":#删除购物车
#             goods_name = input("请输入要删除的商品名称")
#
#             if goods_num not in shopping_cart:
#                 print("该商品不存在，请重新选择")
#             else:
#                 del shopping_cart[goods_name]
#                 print("该商品删除完毕")
#         case "4":#遍历购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info=shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品名称：{goods_info['num']}")
#
#         case "5":#退出购物车
#             print("bye")
#             break#退出循环
#         case "_": #匹配其他所有情况
#             print("非法操作，不支持！！！")

"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用教务管理系统 ~")

student_scores = {}

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行的具体操作
    choice = input("请选择要执行的操作(1-7): ")
    match choice:
        case "1":  # 添加学生信息
            student_name = input("请输入学生姓名: ")
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))

            # 如果学生存在, 则不执行添加, 提示信息
            if student_name in student_scores:
                print("该学生已存在, 请重新选择 ~")
            else:
                student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print("学生信息添加完毕 ~")

        case "2":  # 修改学生信息
            student_name = input("请输入要修改的学生姓名: ")
            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
                continue

            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print("学生信息修改完毕 ~")

        case "3":  # 删除学生信息
            student_name = input("请输入要删除的学生姓名: ")

            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                del student_scores[student_name]
                print("学生信息删除完毕 ~")

        case "4":  # 查询学生信息
            student_name = input("请输入要查询的学生姓名: ")

            # 如果学生不存在, 则提示错误信息
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                student_info = student_scores[student_name]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info['chinese']}, 数学成绩: {student_info['math']}, 英语成绩: {student_info['english']}")

        case "5":  # 列出所有学生
            for student_name in student_scores.keys():
                student_info = student_scores[student_name]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info['chinese']}, 数学成绩: {student_info['math']}, 英语成绩: {student_info['english']}")

        case "6":  # 统计班级成绩
            if not student_scores:
                print("系统中暂无学生信息，请先添加学生 ~")
                continue

            # 初始化统计变量
            chinese_scores = []
            math_scores = []
            english_scores = []

            # 收集所有成绩
            for student_name, scores in student_scores.items():
                chinese_scores.append(scores['chinese'])
                math_scores.append(scores['math'])
                english_scores.append(scores['english'])

            # 计算最高分、最低分、平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores) / len(english_scores)

            # 找出最高分和最低分的学生
            chinese_max_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_max]
            chinese_min_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_min]

            math_max_students = [name for name, scores in student_scores.items() if scores['math'] == math_max]
            math_min_students = [name for name, scores in student_scores.items() if scores['math'] == math_min]

            english_max_students = [name for name, scores in student_scores.items() if scores['english'] == english_max]
            english_min_students = [name for name, scores in student_scores.items() if scores['english'] == english_min]

            # 输出统计结果
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_students}")
            print(f"     最低分学生: {chinese_min_students}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_students}")
            print(f"     最低分学生: {math_min_students}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_students}")
            print(f"     最低分学生: {english_min_students}")
            print("========================")

        case "7":  # 退出系统
            print("Bye ~")
            break

        case "_":  # 匹配其他所有情况
            print("非法操作, 不支持!!!")


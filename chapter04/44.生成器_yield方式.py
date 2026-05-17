"""
目的：节省内存

实现方式：
    1.推导式写法
    2.yield关键字
"""

my_g=(i for i in range(1,11))
def my_fun():
#     my_list = []
#     for i in range(1,11):
#         my_list.append(i)
#     return my_list
    #效果同上
    for i in range(1,11):
        yield i

my_g2=my_fun()
print(type(my_g2))      #<class "generator">
print(next(my_g2))
print(next(my_g2))
print("_"*23)
for i in my_g2:
    print(i)

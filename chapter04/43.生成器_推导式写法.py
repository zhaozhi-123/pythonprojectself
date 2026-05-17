"""
目的：节省内存

实现方式：
    1.推导式写法
    2.yield关键字
"""
import sys

#生成1-10之间的整数
my_generator=(i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print("_"*23)

#生成1-10之间的偶数
my_generator2=(i for i in range(1,11) if i%2==0)
print(my_generator2)
print("_"*23)

#从生成器中获取数据
#思路1：next()
print(next(my_generator2))      #2
print(next(my_generator2))      #4
print("*"*23)
for i in my_generator2:
    print(i)
print("_"*23)

#验证生成器的目的：可以减少内存占用
my_list=[i for i in range(1000)]
my_generator3=[i for i in range(1000)]
print(type(my_generator3),type(my_list))

#查看my_list的内存空间占用
print(f"my_list的内存占用{sys.getsizeof(my_list)}")
print(f"my_generator3的内存占用{sys.getsizeof(my_list)}")
print("_"*23)

for i in my_generator3:
    print(i)




"""
迭代器：自定义的类，只要重写了__iter__()和__next__()方法，就可以称为迭代器

目的：隐藏底层逻辑/惰性加载（用时才会获取）
"""

#range用法
for i in range(1,6):
    print(i)
print("_"*23)

#自定义迭代器
class MyIterator:
    def __init__(self, start,end):
        self.current_value = start
        self.end=end

    #重写iterator魔法方法，返回当前对象（迭代器对象）
    def __iter__(self):
        return self

    #重写next方法
    def __next__(self):
        #判断当前值范围是否合法
        if self.current_value >= self.end:
            raise StopIteration()#抛出异常，迭代结束

        value = self.current_value
        self.current_value=self.current_value + 1
        return value

        #效果同上
        # self.current_value += 1
        # return self.current_value - 1

#创建迭代器对象，并遍历
for i in MyIterator(1, 6):
    print(i)


#next函数
my_iterator = MyIterator(10,13)
print(next(my_iterator))    #10
print(next(my_iterator))    #11
print(next(my_iterator))    #12
# print(next(my_iterator))    #抛出异常，迭代结束





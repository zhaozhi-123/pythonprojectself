def fun1():
    print("fun1...running...")
    fun2()

def fun2():
    print("fun2...running...")
    fun3()

def fun3():
    print("fun3...running...")
    print(my_color)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("错误代码：",e)


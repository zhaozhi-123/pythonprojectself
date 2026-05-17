#__all__指定from...import*导入的是哪些功能
__all__=['log_separator1','log_separator3','PI','NAME']
#常量（名称为全部大写）
PI=3.14
NAME="唤鹿"

#函数
def log_separator1():
    print("-"*30)   #"-"重复输出30次

def log_separator2():
    print("+"*30)

def log_separator3():
    print("#"*30)

def log_separator4():
    print("*"*30)

#测试函数
#__name__:内置模块（__name__值为"__main__";该模块被导入时，__name的值就是模块名）
#执行当前文件， 则会执行如下代码;若被当做模块导入，则如下代码不执行
if __name__ == '__main__':
    log_separator1()


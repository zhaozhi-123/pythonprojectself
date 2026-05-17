#用于程序的入口文件
from studentcms import StudentCMS
#程序的主入口
if __name__=="__main__":
    #创建对象
    cms=StudentCMS()
    #启动程序
    cms.start()

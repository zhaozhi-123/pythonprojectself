#导入模块
# import utils.my_fun
#
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()


# from utils import my_fun
#
# my_fun.log_separator1()
# my_fun.log_separator3()
# my_fun.log_separator2()

#注意：通过from  utils import *导入包下所有模块时，需要在__init__.py文件中添加__all__=[]
# from  utils import *
#
# my_fun.log_separator1()
# my_fun.log_separator2()
#
# print(my_var.PI)
# print(my_var.NAME)


#导入模块功能
#相对路径：从当前文件所在目录开始查找
# from utils.my_fun import log_separator1,log_separator3
#绝对路径：从项目的根目录下开始查找
from chapter02.utils.my_fun import log_separator1,log_separator3

log_separator1()
log_separator3()


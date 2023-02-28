# This is a sample Python script.


#这是单行注释
"""
这是多行注释
这是多行注释
"""
'''
也可以用三个单引号来进行多行注释
'''
from sys import argv,path  #  导入特定的成员

if __name__ == '__main__':
    x = input("请输入X的值：")
    print(type(x))
    print(type(int(x)))
    print(x)

    print('================python from import===================================')
    print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
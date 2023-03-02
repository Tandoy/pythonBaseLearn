# This is a sample Python script.


# 这是单行注释
"""
这是多行注释
这是多行注释
"""
'''
也可以用三个单引号来进行多行注释
'''
if __name__ == '__main__':
    def printStr(str):
        print(str)
        return


    printStr("测试自定义函数")


    def ChangeInt(a):
        a = 10


    b = 2
    ChangeInt(b)
    print(b)  # 结果是 2 numbers 类型是不可变对象


    def changeme(mylist):
        "修改传入的列表"
        mylist.append([1, 2, 3, 4])
        print("函数内取值: ", mylist)
        return


    # 调用changeme函数
    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值: ", mylist)  # 列表是可变对象


    # 匹配传参
    def printinfo(name, age):
        "打印任何传入的字符串"
        print("Name: ", name)
        print("Age ", age)
        return


    # 调用printinfo函数
    printinfo(age=50, name="miki")


    # 缺省参数
    def printinfo(name, age=35):
        "打印任何传入的字符串"
        print("Name: ", name)
        print("Age ", age)
        return


    # 调用printinfo函数
    printinfo(age=50, name="miki")
    printinfo(name="miki")


    # 不定长参数
    def printinfo(arg1, *vartuple):
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        for var in vartuple:
            print(var)
        return


    # 调用printinfo 函数
    printinfo(10)
    printinfo(70, 60, 50)

    # 匿名函数
    sum = lambda r1, r2: r1 + r2
    print("Value of total : ", sum(10, 20))
    print("Value of total : ", sum(20, 20))


    # 函数返回值
    def sum(arg1, arg2):
        # 返回2个参数的和."
        total = arg1 + arg2
        print("Inside the function : ", total)
        return total


    # 调用sum函数
    total1 = sum(10, 20)
    print("Outside the function : ", total1)

    # 局部变量 + 全局变量
    total = 0  # 全局变量


    def sum2(arg1, arg2):
        # 返回2个参数的和."
        total = arg1 + arg2  # 局部变量
        print("Inside the function local total : ", total)
        return total


    # 调用sum函数
    sum2(10, 20)
    print("Outside the function global total : ", total)

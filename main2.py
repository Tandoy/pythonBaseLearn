# This is a sample Python script.


# 这是单行注释
"""
这是多行注释
这是多行注释
"""
'''
也可以用三个单引号来进行多行注释
'''
from sys import argv, path  # 导入特定的成员

if __name__ == '__main__':
    x = input("请输入X的值：")
    print(type(x))
    print(type(int(x)))
    print(x)

    print('================python from import===================================')
    print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

    age = int(input("请输入你家狗狗的年龄: "))
    if age < 0:
        print("请输入正确的年龄。")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄： ", human)

    a = [1, 2, 3, 4, 'ff']
    print(a + ['kobe'])

    # set
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
    print(student)

    if "Tomm" in student:
        print("get it")
    else:
        print("not get it")

    a = set('abra')
    b = set('alacz')
    print(a)
    print(b)

    # 字典
    tel = {'Jack': 1557, 'Tom': 1320, 'Rose': 1886}
    print(tel['Jack'])
    print(sorted(tel.keys()))

    # 循环
    str = ['Mary', 'had', 'a', 'little', 'lamb']
    str2 = ['kobe']
    str.extend(str2)
    for i in range(len(str)):
        print(i, str[i])

    # 迭代器
    it = iter(str)
    for x in it:
        print(x)

    # 列表推导式
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print([x.strip() for x in freshfruit])

    # 同时遍历两个或更多的序列，可以使用 zip() 组合
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
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
    class MyClass:
        """一个简单的类实例"""
        i = 12345

        def f(self, str):
            return 'hello world ' + str


    # 实例化类
    x = MyClass()

    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)
    print("MyClass 类的方法 f 输出为：", x.f('kobe'))


    class people:
        # 定义基本属性
        name = ''
        age = 0
        # 定义私有属性,私有属性在类外部无法直接进行访问
        __weight = 0

        # 定义构造方法
        def __init__(self, n, a, w):
            self.name = n
            self.age = a
            self.__weight = w

        def speak(self):
            print("%s 说: 我 %d 岁。" % (self.name, self.age))


    # 单继承示例
    class student(people):
        grade = ''

        def __init__(self, n, a, w, g):
            # 调用父类的构函
            people.__init__(self, n, a, w)
            self.grade = g

        # 覆写父类的方法
        def speak(self):
            print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


    s = student('ken', 10, 60, 3)
    s.speak()
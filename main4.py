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
    def this_fails():
        x = 1 / 0


    try:
        this_fails()
        # raise NameError('HiThere')
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
    else:  # 会在没有异常被捕获时执行
        print("......")


    class MyError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)


    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My exception occurred, value:', e.value)


    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        except TypeError:
            print("unsupported operand type(s)!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")


    divide(2, 0)

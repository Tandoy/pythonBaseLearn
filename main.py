# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyword

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#这是单行注释
"""
这是多行注释
这是多行注释
"""
'''
也可以用三个单引号来进行多行注释
'''

if __name__ == '__main__':
    str  = "W3Cschool"
    print(type(str ))
    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])  # 输出从第三个开始后的所有字符
    print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
    print(str * 2)  # 输出字符串两次
    print(str + '你好')  # 连接字符串

    print('------------------------------')

    print('hello\nW3Cschool')  # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nW3Cschool')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
    print_hi(keyword.kwlist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

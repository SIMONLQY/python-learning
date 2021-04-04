# 1.使用了try-except代码块，及时出现异常，程序也将运行，并显示你编写的友好的错误信息
# 这个东西在编写程序模块可能作用不大，但如果要考虑用户体验，则有很大好处
try:
    print(5 / 0)
except ZeroDivisionError:
    print("you can't divide by zero!")
print(5 / 1)

# 2.try-except-else代码块
# print("Give me two numbers, and i will divide them")
# print("enter q to quit")
# while True:
#     number_1 = input('please input the first number:')
#     if number_1 == 'q':
#         break
#     number_2 = input('please input the second number:')
#     if number_2 == 'q':
#         break
#     try:  # 只包含可能包含错误的代码
#         answer = float(number_1) / float(number_2)
#     except ZeroDivisionError:
#         print("you can't divide zero")
#     else:  # 依赖于try代码块成功执行的代码都应放到else代码块
#         print(answer)

# 3.处理FileNotFoundError异常
file_name = 'wen_jian_1.txt'
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("file is not found")
else:
    print(contents)
# 4.分析文本
# split方法可根据一个字符串产生一个单词列表
file_name = 'alice in wonderland.txt'
with open(file_name) as file_object:
    contents = file_object.read()
    contents_words = contents.split()
    print(len(contents_words))
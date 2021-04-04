# 1.从文件中读取数据
# 任何方式使用文件首先要打开（open）它
# 关键词with在不再需要访问文件后将其关闭(python自行决定close时间)
with open('wen_jian_1.txt') as file_object:
    contents = file_object.read()  # 一个很长的str对象
    print(contents)

# 2.windows系统要用反斜杠\而不是斜杠/
# 3.逐行读取（用于寻找某种特定信息）
file_name = 'wen_jian_1.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)  # 这样空白行会很多，因为print自己加一个换行符

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 4.创建一个包含文件各行内容的列表
# with打开的文件对象只在with内部有用
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 5.数字中是否包含你的生日
pi_string = ''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
# birthday = input('please enter your birthday, in the form mmddyy:')
# if birthday in pi_string:
#     print("yes, it's in")
# else:
#     print("sorry, no")

# 6.写入文件
# 实参'w'告诉open我们要以写入的方式打开文件，其余含有：
# 'r'读取模式(默认)
# 'a'附加模式
# 'r+'读取和写入
# 'w'要注意：如果文件已经存在，会清空.
# 'w'只有这个参数会在不存在这个文件时创建。
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('i love programming') # write不会在行位添加换行符

with open(file_name,'w') as file_object:
    file_object.writelines(lines)#writelines可接受list为参数，除此之外和write相同
    file_object.writelines('\ni love you\n')
    file_object.write('asdf')

with open(file_name,'a') as file_object:
    file_object.write('\nasdf')


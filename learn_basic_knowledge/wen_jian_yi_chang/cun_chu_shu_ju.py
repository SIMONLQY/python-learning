import json

# 1.模块json能够让你将简单的python数据结构转移到文件中，并在程序再次运行时加载该
# 文件中的数据，还可以使用json在python程序间共享数据，且json数据格式并非python专用

# 2.json.dump()接受两个参数：要存储的数据以及可用于存储数据的文件对象
numbers = [1, 2, 3, 4, 5, 6]
file_name = 'numbers.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)
with open(file_name) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# 3.保存和读取用户生成的数据
file_name = 'usr_name.json'
try:
    with open(file_name) as f_obj:
        user_name = json.load(f_obj)
except FileNotFoundError:
    print("you haven't got a name")
    user_name = input("plese enter your name:")
    with open(file_name,'w') as f_obj:
        json.dump(user_name, f_obj)
        print("your name is " + user_name)
else:
    print("your name is " + user_name)

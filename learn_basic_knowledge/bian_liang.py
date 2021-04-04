#1.字符串函数，title将单词首字母大写；upper全大写；lower全小写
name = "ada asd"
print(name.title())
print(name.upper())
print(name.lower())

#2.字符串与字符串之间可以通过 + 号拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +  last_name
print("Hello, " + full_name.title() + " !")

#3.添加/删除空白
print("\tpython\n1")
favorite_language = "python "
print(favorite_language.rstrip())#lstrip删除最左侧空白，r删最右边，strip删左右



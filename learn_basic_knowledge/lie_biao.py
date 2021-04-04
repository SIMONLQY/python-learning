#1.索引-1返回列表最后一个元素,且可以以此类推
my_list = ['i', 'love', 'games']
print(my_list[-1])
print(my_list[-2])

#2.在列表中添加,插入和删除元素
my_list = ['i', 'love', 'games']
my_list.append(1)#添加
print(my_list)
my_list.insert(0,2)#插入
print(my_list)
del my_list[0]#删除
print(my_list)
pop_element = my_list.pop(0)#如果你想在从列表中移除这个元素的同时保留这个元素就用pop，否则用del
print(my_list,pop_element)
my_list.remove('love')#remove根据值删除元素
print(my_list)

#3.组织列表
my_list = [1,2,3]
my_list.sort()#sort对列表进行永久性排序，按照字母顺序（或者数字顺序）；可传递参数reverse = True使反向排序
print(my_list)
print(sorted(my_list,reverse = True))#sorted可以对list进行临时排序
my_list.reverse()#倒着列表，永久性
print(my_list,len(my_list))

#4.数字列表创建
#range(1,5)只包含1~4.range可以方便的操作某个范围中的整数
numbers = list(range(1,6,2)) #利用list(range())可以方便的生成列表,第三个参数为步长
print(numbers)

#5.对数字列表进行统计计算
digits = list(range(1,5000000))
print(max(digits))
print(sum(digits))

#6.列表解析
#要使用这种方法，首先要指定一个列表名，然后制定一个方括号，然后定一个表达式(value**2),
#接着后面跟一个for循环的条件句，用于给表达式提供值
squares = [value**2 for value in range(1,11)]
print(squares)


#7.使用列表的一部分
digits = list(range(1,5000))
print(digits[0:60])
print(digits[:2])
digits_2 = digits[:] #可以这样来复制列表(这时候有两个列表而不是一个列表两个名字，如果直接写等号就是只有一个列表)
print(digits_2)
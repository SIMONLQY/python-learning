# #1.input函数
# message = input('please give me your name: ')
# print(message)
#
# #2.使用int来获取数值输入
# age = input("how old are you? ")
# age = int(age)
# print(age<1)
#
# #3.求模运算符%
# #4.while循环:
# count_number = 1
# while count_number<5:
#     print(count_number)
#     count_number+=1
#
# #5.让用户选择何时退出：
# msg = ''
# while msg!='quit':
#     msg = input("input anything you want,and input quit to quit:")
#     if msg != 'quit':
#         print(msg)
#
# #6.利用标志（这样while循环看似一个判别条件，实际上这个判别条件为标志时可以再很多地方改变以结束while循环）
# prompt = 'Tell me something,and i will repeat it back to you:'
# prompt+='\nEnter quit to end the program.\n'
# active = True
# while active==True:
#     msg = input(prompt)
#     if msg=='quit':
#         active=False
#     else:
#         print(msg)
#
# #7.使用break退出循环(只能退出一层循环)
# for i in range(5):
#     print(i)
#     for j in range(5):
#         print(i,j)
#         if i==2:
#             break
#
#8.遍历列表同时修改元素要用while循环:
unconfirmed_usrs = ['alice', 'simon', 'jack']
confirmed_usrs = ['marcha']
while unconfirmed_usrs:
    current_usr = unconfirmed_usrs.pop()
    confirmed_usrs.append(current_usr)
# for i,un_usr in enumerate(unconfirmed_usrs):
#for行不通因为要删除元素要么用pop则要倒叙删除，难以利用；要么用序号，而序号只会增加。
#     confirmed_usrs.append(un_usr)
#     del unconfirmed_usrs[i]

print(unconfirmed_usrs,confirmed_usrs)


#9.字典的key不能重复,否则会自动合并
my_zidian = {'color':'yellow','color':'yell'}
print(my_zidian)
#1.位置实参
def function_1(name,color):
    print('my name is:'+name + ' ' + 'my color is:' + color)

function_1('liqingyao', 'blue')

#2.关键词实参：
function_1(color = 'blue', name = 'liqingyao')

#3.默认值：（定义函数时候，无默认值的形参在前）
#默认值也可以让参数变成可选的，只要设置成空值‘’就行了
def function_2(name, color ='blue', height = ''):
    if height:
        print(height)
    print('my name is:'+name + ' ' + 'my color is:' + color)

function_2('liqingyao',height = 14)

#4.函数能直接修改列表
digits = list(range(500))
def get_digits_changed(digits):
    digits.append(501)
    return digits
get_digits_changed(digits)
print(digits[-1])

#5.可禁止函数修改列表（只要使用函数时传递列表的复制即可）
digits = list(range(500))
get_digits_changed(digits[:])
print(digits[-1])

#6.预先不知道要传递的实参数量时，用指针
#形参*toppings让python创建一个空元祖，包含所有传进来的参数
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)
make_pizza(1,2,3,4)

7.#任意数量实参与位置实参混合使用时，指针形参要放到最后：
def my_print(name,*toppings):
    print(name)
    print(toppings)

my_print('liqingyao', 1,2,3, 'asdf')

#8.使用任意数量的关键词实参(**会让python创建一个名为usr_info的空字典)
def build_profile(first,last,**usr_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key,value in usr_info.items():
        profile[key] = value
    return profile

my_info = build_profile('li','qingyao',location = 'princeton',filed = 'physics')
print(my_info)







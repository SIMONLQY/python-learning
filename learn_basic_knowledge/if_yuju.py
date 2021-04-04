#1.检查特定值是否在列表中
digist = list(range(1,500))
if 200 in digist:
    print(1)
if 600 not in digist:
    print(1)

#2.#if-elif-...-else结构：
if 2000 in digist:
    print(1)
elif 200000 in digist:
    print(2)
elif 3 in digist:
    print(3)
else:
    print(0)

#3.确认列表是不是空的
non_list = [1]
if non_list:
    print("there is something here")

#4.
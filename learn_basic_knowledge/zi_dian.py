#1.字典增加元素：
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 5
alien_0['y_position'] = 6
print(alien_0)

#2.删除字典中的键值对
del alien_0['color']
print(alien_0)

#3.遍历字典
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermin',
    'relast':'fermin',
}
for key,value in user_0.items():#分开获取键值对
    print('key:' + key,',value:' + str(value))
for item in user_0.items(): #一并获取键值对
    print(item)

for key in user_0.keys(): #只获取键
    print(key)
for value in user_0.values():#只获取值
    print(value)
for key in sorted(user_0.keys()): #按照字母顺序获取键
    print(key)
for value in set(user_0.values()):#set函数可将value的重复项合并
    print(value)

#4.嵌套
aliens = []
for i in range(30):
    new_alien = {'color':'yellow','points':5}
    aliens.append(new_alien)
print(len(aliens))
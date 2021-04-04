# 1.类里面只能定义函数
# __init__()函数比较特殊，在对象创建时候自动运行，且self形参必不可少且必须在第一位
#类名一般用驼峰命名法（每个单词首字母大写而不用下划线）
# 2.修改属性的值
class Car():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.odemeter = 0

    def update_odemeter(self, meter):
        self.odemeter = meter

    def increase_odemeter(self, meter):
        self.odemeter += meter


my_car = Car('bmw', 'yellow')
print(my_car.odemeter)
my_car.odemeter = 1  # 直接修改
print(my_car.odemeter)
my_car.update_odemeter(5)  # 通过类内定义的方法修改
print(my_car.odemeter)
my_car.increase_odemeter(5)  # 通过递增
print(my_car.odemeter)


# 3.将实例用作属性
# 例如不断给Electirccar类添加属性和方法时发现太多了，可以将一些属性或者方法
# 提取出来成一个Battery类，然后将其作为Electriccar的一个属性
class Battery():
    def __init__(self, bat_size=70):
        self.bat_size = bat_size

    def describe_battery(self):
        print("this battery's size is:" + str(self.bat_size))

# 4.继承
# 创建子类的实例时，首先要给父类继承下来的属性赋值
# 子类添加属性一般是通过重写__init__()方法，添加方法就直接添加
class ElectricCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.bat = Battery()


my_electriccar = ElectricCar('bmw', 'blue')
my_electriccar.update_odemeter(5)
print(my_electriccar.odemeter)
my_electriccar.bat.describe_battery()
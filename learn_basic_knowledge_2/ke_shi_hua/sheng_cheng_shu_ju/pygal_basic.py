from random import randint
import pygal


# 尝试用pygal画矢量图，可自动适应观看者的屏幕
# 用pygal可视化掷骰子的结果
# 骰子类
class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的数字"""
        return randint(1, self.num_sides)


# 掷骰子
die_1 = Die()
die_2 = Die()
results = []
for i in range(1001):
    results.append(die_1.roll() + die_2.roll())
# 分析结果
# frequencies = {}
frequencies = []
for i in range(2, die_1.num_sides * 2 + 1):
    # frequencies[str(i)] = results.count(i)
    frequencies.append(results.count(i))
print(frequencies)
# 绘制直方图
hist = pygal.Bar()  # 条形图实例
hist.title = "Results of rolling one D6 1000 times"
x_labels = list(range(2,die_1.num_sides * 2 + 1))
x_labels = [str(value) for value in x_labels]
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Results"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

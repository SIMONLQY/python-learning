from random import choice
import matplotlib.pyplot as plt


# 1.随机漫步是这样行走得到的路径：每次行走都完全是随机的没有明确的方向，
# 结果是由一系列随机决策决定的。
class RandmWalk():
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        self.xlabels = [0]
        self.ylabels = [0]

    def fill_walk(self):
        """计算随机漫步中所包含的点"""
        while len(self.xlabels) < self.num_points:
            # 决定前进方向以及沿着这个方向所前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            if x_distance == 0 and y_distance == 0:
                continue
            next_x = self.xlabels[-1] + x_distance * x_direction
            next_y = self.ylabels[-1] + y_distance * y_direction
            self.xlabels.append(next_x)
            self.ylabels.append(next_y)


my_random_walk = RandmWalk(5e4)
my_random_walk.fill_walk()
# 调整尺寸以适应屏幕
plt.figure(figsize=(10,6))
plt.scatter(my_random_walk.xlabels,
            my_random_walk.ylabels,
            edgecolors='none',
            c=list(range(1, int(5e4+1))),
            cmap=plt.cm.Blues,
            s=1)
# 重新绘制起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(my_random_walk.xlabels[-1],
            my_random_walk.ylabels[-1],
            c='red',
            edgecolors='none')
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()

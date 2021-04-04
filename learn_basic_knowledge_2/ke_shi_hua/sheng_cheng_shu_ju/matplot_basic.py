import matplotlib.pyplot as plt

# 1.使用matplot画折线图
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=3)
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=22)
plt.xlabel("Value", fontsize=20)
plt.ylabel("Square of Value", fontsize=20)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

# 2.使用scatter()绘制散点图并设置其样式
x_values = [2, 4, 5, 6, 8]
y_values = [2, 4, 5, 6, 8]
plt.scatter(x_values, y_values, s=100)
# plt.scatter(2,4,s=200)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=20)
plt.xlabel('values', fontsize=20)
plt.ylabel('square values', fontsize=20)
# 设置刻度标签的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

# 3.自动计算数据
x_values = list(range(1, 1001))
y_values = [value ** 2 for value in x_values]
# edgecolors设置点的轮廓颜色
# c填充实心颜色，也可以传递（0.5,0.5,0.5）分别表示红绿蓝占比,或者'red'
plt.scatter(x_values, y_values, c='red', s=1, edgecolors='none')
# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# 设置图表标题并给坐标轴加上标签
plt.xlabel("Values", fontsize=20)
plt.ylabel("Square of values", fontsize=20)
plt.title("Square", fontsize=20)
# 设置刻度标签的大小
plt.tick_params(axis="both", labelsize=15)
plt.show()

# 4.颜色映射+图片保存
# 较浅的颜色代表较小的值
x_values = list(range(1, 1001))
y_values = [value ** 2 for value in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# 保存图片，第二个参数表示删除周围白色区域
# 要在show之前保存图片，show之后plt清空重启
plt.savefig('asdf.png', bbox_inches='tight')
plt.show()

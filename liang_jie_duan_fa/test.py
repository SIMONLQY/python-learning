import numpy as np

# test 1 矩阵的一些操作
A = [[0, 1, 2],
     [0, 2, 3],
     [0, 3, 3]]
A = np.array(A)
B = [0, 1]
print(A[:, B])
b = np.array([2,0])
print(np.size(b))
print(b.any() == 0)
# test 2 单纯形法

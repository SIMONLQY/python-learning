# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#  求解线性方程组

from scipy import linalg
import numpy as np

# x1 + x2 + 7*x3 = 2
# 2*x1 + 3*x2 + 5*x3 = 3
# 4*x1 + 2*x2 + 6*x3 = 4

A = np.array([[5, 5327], 
              [5327, 7277699]])  # A代表系数矩阵
b = np.array([271.4, 369321.5])  # b代表常数列
x = linalg.solve(A, b)
print(x)




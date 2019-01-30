# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:17:20 2018

@author: Administrator
"""

from cvxopt import matrix, spmatrix, solvers


# 创建密集矩阵
A = matrix([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], (2,3))
#  B = matrix([ [1.0, 2.0], [3.0, 4.0] ])  
print(A)
print(A.size)

# 索引（单参数索引和双参数索引），索引集可以是整数，列表，整数矩阵或切片
print(A[[0,1],[0,2]])
print(A[1,:])

# 单参数索引，每列每列读取
A[::4] = -1
print(A)


# 创建稀疏矩阵
# 1.在0,0   2.在1,1
D = spmatrix([1., 2.], [0, 1], [0, 1], (4,2))
print(D)



#numpy.array和matrix可以互相初始化
# numpy.array(matrix)
# matrix(numpy.array)

# 求解线性问题
A = matrix([ [-1.0, -1.0, 0.0, 1.0], [1.0, -1.0, -1.0, -2.0] ])
b = matrix([ 1.0, -2.0, 0.0, 4.0 ])
c = matrix([ 2.0, 1.0 ])
sol=solvers.lp(c,A,b)


# solvers.qp解决二次方程


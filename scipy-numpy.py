# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:36:53 2018

@author: Administrator
"""

import scipy.stats as stats
import numpy as np

# 初始化
# 生成20个小于100的随机整数
X = np.random.randint(100, size=20)

X1 = np.random.randn(100)

# 正太分布
X2 = np.random.normal(0,0.1,1000)


X3 = np.array([1,2,3,4,5])

# 创建等差数列，-6到6，300个数
X4 = np.linspace(-6,6, 300)

# 删除第几纬度上的第几条数据
np.delete(X3, 1, axis = 0)

# 第几纬度上的第5个位置插入数据6
np.insert(X3, 5, 6, axis = 0) #等价于np.append(X3,6,axis=0) 

# 相关系数
np.corrcoef(X1,X1)

# 协方差
np.cov(X1,X1)

x1 = [1, 2, 2, 3, 4, 5, 5, 7]

# 排序
x2 = np.sort(x1)

# 最大值和最小值之间的差异
np.ptp(x1)

# 算术平均值
np.mean(x1)

# 中位数
np.median(x1)

# 方差
np.var(x1)

# 标准差
np.std(x1)



# 垂直组合 
#np.vstack((up,down)) up, down 表示数据在上还是在下，类似于堆栈 
# 水平组合 
#np.hstack((left, right)) left right 表示数据在左还是在右 
# 行组合（对象：一维数组） 
#np.row_stack((up,down)) 
#列组合（对象：一维数组） 
#np.column_stack((left,right)) 
# 深度组合 
#np.dstack((a,b)) 
#垂直分割(vstack 与 vsplit 操作可逆) 
#u,m,d = np.vsplit(v,3) # 3表示分割后的个数 
#水平分割(hstack 与 hsplit 操作可逆) 
#l,m,r = np.hsplit(v,3) 
#深度分割 ——–(操作不可逆) 
#x,y = np.dsplit(d,2) 
#可逆需进行 x.T[0].T 的操作


#np.newaxis在使用和功能上等价于None，其实就是None的一个别名

newx = np.arange(3) #[0,1,2]
newx.shape #(3,)

#newx[:, np.newaxis]
newx2 = newx[:, np.newaxis] #[[0],[1],[2]]
newx2.shape #(3,1)

newx3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
newx3[:, 1]   #这里是一个行，shape为(3,)
#需要索引多维数组的某一列时
newx3[:, 1][:, np.newaxis] #[[2],[6],[10]]


#切片中加None等于该维不进行切片，而是将该维整体作为数组元素处理
a = np.array([[1,2],[3,4]])
print(a.shape) #(2,2)
print(a[:,None].shape) #(2,1,2) [[[1,2]], [[3,4]]]



per = np.array([[10, 7, 4], 
                [3, 2, 1]])

#表示30%的数据x小于5.1，70%大于5.1
print(np.percentile(per, 30, axis=0)) #array([[ 5.1,  3.5,  1.9]])



cum_a = np.arange(10)
#累加
print(np.cumsum(cum_a)) #[0 1 3 6 10 15 21 28 36 45]
#累乘（加1是防止数据有0）
print(np.cumprod(cum_a+1)) #[1 2 6 24 120 720 5040 40320 362880 3628800]


#矩阵
#np.matrix
mul_a = np.array([[1, 2], 
                  [3, 4]])
mul_b = np.array([[0, 1], 
                  [2, 3]])
#无论矩阵还是数组都是对应位置现乘
np.multiply(mul_a, mul_b) # [[0,2][6,12]]


#对数组和矩阵都实现点乘
np.dot(mul_a,mul_b)

#数组对应位置相乘
mul_a*mul_b # [[0,2][6,12]]

#矩阵对应矩阵运算
print((np.mat(mul_a))*(np.mat(mul_b))) # [[4, 7],[8, 15]]



# 众数
stats.mode(x1)[0][0]

# 几何平均值
stats.gmean(x1)

# 调和平均值
stats.hmean(x1)

# 偏度值
#stats.skew(X4)


#正态分布
"""
stats.A.B
A:分布类型
beta        beta分布
f           F分布
gamma       gam分布
poisson	    泊松分布
hypergeom	超几何分布
lognorm	    对数正态分布
binom	    二项分布
uniform	    均匀分布
chi2	    卡方分布
cauchy	    柯西分布
laplace	    拉普拉斯分布
rayleigh	瑞利分布
t	        学生T分布
norm	    正态分布
expon	    指数分布
cosine      余弦分布 ...

B:处理函数
rvs   产生服从指定分布的随机数
pdf   概率密度函数
cdf	  累计分布函数。
sf    残存函数（1 - cdf）
ppf   分位点函数
isf   逆残存函数（sf逆）
stats(moments ='mv')	平均值（'m'），方差（'v'），偏斜（'s'）和/或峰度（'k'）
fit   通用数据的参数估计。
median   分布中位数
mean     分布的平均值
var      分布的方差
std      分布的标准差

"""
# 获取正态分布概念密度函数
#print(stats.norm.pdf(X4))

# 对数概念密度函数
#stats.lognorm.pdf(x，s，loc = 0，scale = 1)


#稀疏矩阵
#scipy.sparse


"""
包含许多优化算法
使用各种算法(例如BFGS，Nelder-Mead单纯形，牛顿共轭梯度，COBYLA或SLSQP)的无约束和约束最小化多元标量函数(minimize())
全局(蛮力)优化程序(例如，anneal()，basinhopping())
最小二乘最小化(leastsq())
曲线拟合(curve_fit())
标量单变量函数最小化(minim_scalar())
根查找(newton())
使用多种算法(例如，Powell，Levenberg-Marquardt混合或Newton-Krylov等大规模方法)的多元方程系统求解(root)
"""
import scipy.optimize as op

#非线性方程组求解
"""
计算非线性方程组：
    5x1+3 = 0
    4x0^2-2sin(x1x2)=0
    x1x2-1.5=0
"""
## 误差函数
def fun(x):
    x0,x1,x2 = x.tolist()
    return [5*x1+3, 4*x0**2-2*np.sin(x1*x2), x1*x2-1.5]

result = op.fsolve(fun,[1,1,1]) # [-0.70622057    -0.6    -2.5]

"""
求根
2x + 2cos(x) = 0 
"""
def func(x):
   return 2*x + 2 * np.cos(x)
sol = op.root(func, 0.3)
print(sol)

#最小二乘拟合
x = np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
y = np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
def residual(p):
    k,b = p
    return y-(k*x+b)

#传入误差函数和函数初始值
r = op.leastsq(residual,[1,0])
print(r)

#局部最小值
"""
fun(x0,args)
optimize.minimize(fun,x0,args,method,jac,hess,constraints=({},{}),option={'maxiter':0,'disp':True}) 
fun：函数的表达式计算 
x0：初始值
args: 参数传递
method：最小化的算法 
jac：雅各比矩阵
hess：黑塞矩阵
constraints: 约束定义（仅适用于COBYLA和SLSQP）
options: 求解器选项字典
"""

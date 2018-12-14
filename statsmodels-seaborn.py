# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:44:57 2018

@author: Administrator
"""

import numpy as np
import statsmodels.tsa.stattools as sts
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import statsmodels.api as sm
from statsmodels import regression

X = np.random.randn(1000)
Y = np.random.randn(1000)

#plt.scatter(X,Y)
#plt.show()

# 协方差
# np.cov

# 相关系数
#np.corrcoef(X,Y)[0,1]


X = np.random.randn(1000)
Y = X + np.random.normal(0,0.1,1000)

#plt.scatter(X,Y)
#plt.show()
#print(np.corrcoef(X,Y)[0,1])

# 设置主题：darkgrid，whitegrid，dark，white，ticks，默认是darkgrid
sns.set_style("ticks")
# 设置背景，调色板等
sns.set(style="white", palette="muted", color_codes=True) 
#plt.plot(np.arange(10))  
#plt.show()  

# palette调色板
"""
对图表整体颜色、比例进行风格设置，包括颜色色板等
"""

# 默认颜色块：deep,muted,pastel,bright,dark,colorblind
current_palette = sns.color_palette()
#sns.palplot(current_palette)

# 颜色风格：Accent,Blues,BrBG等等
# 8为颜色色块个数
#sns.palplot(sns.color_palette('Accent',8))
#sns.palplot(sns.color_palette('Paired', 16))

# 设置年度和饱和度，l亮度 s饱和度
#sns.hls_palette(8 , l = .8, s = .5)


# 按照线性增长计算，设置颜色
# 参数：颜色个数   开始颜色（0-3）   颜色旋转角度   颜色伽马值，越大颜色越暗
#      dark,light ---> 值区间0-1，颜色越深   布尔值，默认为False，由浅到深
#sns.cubehelix_palette(8, start = 2, rot = 0, gamma = 2, dark = 0, light = .95, reverse = True)


# 深浅调色板
#sns.light_palette('red')
#sns.dark_palette('red')


# 创建分散颜色
# 参数：起始/终止颜色值   饱和度，值区间0-100   亮度，值区间0-100   颜色个数
#      中心颜色为浅色还是深色('light' 'dark')，默认为light
#sns.diverging_palette(145,280, s=85, l=25, n=7, center='light')


# 直方图的加强版（可显示密度曲线）
#sns.distplot 

# 密度曲线图 
#sns.kdeplot

# 箱型图
#sns.boxplot

# 热点图
#sns.heatmap










# 为模型增加常数项，即回归线在y轴上的截距
X = sm.add_constant(X) 

# 执行最小二乘回归
#est = sm.OLS(Y,X)
est = regression.linear_model.OLS(Y, X)

# 进行模型拟合
est = est.fit()

a = est.params[0]
b = est.params[1]

X = X[:,1]

# 查看模型拟合的结果
est.summary()
    
    
XP = np.linspace(X.min(), X.max(), 100)
Y_hat = XP*b + a
plt.scatter(X, Y, alpha=0.3) # 显示原始数据
plt.plot(XP, Y_hat, 'r', alpha=0.9);  # 添加拟合直线
plt.xlabel('X Value')
plt.ylabel('Y Value')
sns.regplot(XP, Y_hat)
plt.show()




X1 = np.arange(100)

#  X2 = X1^2 + X1
X2 = np.array([i ** 2 for i in range(100)]) + X1

Y1 = X1 + X2

plt.plot(X1, label='X1')
plt.plot(X2, label='X2')
plt.plot(Y1, label='Y1')
plt.legend()

# 使用column_stack连接X1和X2这两个变量, 然后将单位向量作为截距项
X3 = sm.add_constant(np.column_stack((X1, X2)))

# 运行回归模型
results = regression.linear_model.OLS(Y1, X3).fit()

print('Beta_0:', results.params[0])
print('Beta_1:', results.params[1])
print('Beta_2:', results.params[2])

x = np.random.normal(0, 1, 500)
print(np.cumsum(x))


"""
adf检验是用来检验序列是否平稳的方式
"""
x = np.array([1, 2, 3, 4, 5, 6, 7])
# 参数（x，maxlag = None，regression ='c'，autolag ='AIC'，store = False，regresults = False ）
# maxlag 差分次数
# 返回值 (-2.6825663173365015, 0.077103947319183241, 0, 7, {'5%': -3.4775828571428571, '1%': -4.9386902332361515, '10%': -2.8438679591836733}, 15.971188911270618)
result = sts.adfuller(x, 1)
print(result)


# 检验协整性
# sts.coint(X1, X2)

# 比较样本数据是否具有与正态分布一样的偏度和峰度（是否服从正态分布）
#sts.jarque_bera()

    

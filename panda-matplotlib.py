# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:19:44 2018

@author: Administrator
"""

"""
Pandas库是基于NumPy的一种工具
围绕着Series和DataFrame两个核心数据结构展开
Series 和 DataFrame 分别对应于一维的序列和二维的表结构
"""

from pandas import Series, DataFrame
import pandas as pd
from datetime import timedelta, datetime

import numpy as np



#pd.read_excel
#pd.read_csv

#维度查看
#print(analysis_data.shape)

#数据表基本信息（维度、列名称、数据格式、所占空间等）
#print(analysis_data.info)

#列数据
#print(analysis_data['开盘'])

#每一列数据的格式
#print(analysis_data['开盘'].dtype)

#查看某一列空值
#print(analysis_data['开盘'].isnull())

#查看某一列的唯一值
#print(analysis_data['开盘'].unique())

#查看数据表的值
#print(analysis_data.values)

#查看列名称
#print(analysis_data.columns)

#查看前5行数据
#print(analysis_data.head())

#查看后5行数据
#print(analysis_data.tail())

#用数字0填充空值，空值存为NaN，np.nan
#analysis_data.fillna(value=0)

#求均值
#analysis_data['金额'].mean()

#更改数据格式
#astype('int')

#print(analysis_data)


"""
内连接：默认，结果是键的交集
外连接：结果是键的并集，使用NaN填充
左连接: 产生行的笛卡尔积（左边n个a,右边m个a,结果产生m*n行）
右连接：产生行的笛卡尔积


"""
#数据表合并
#pd.merge

#设置索引列
#analysis_data.set_index('总手')

#按照特定列的值排序：
#analysis_data.sort_values(by=['总手'])

#按照索引列排序：
#analysis_data.sort_index()


#按索引值提取区域行数值
#analysis_data.loc[0:3]

#at的使用方法与loc类似，但只能访问单个元素
#at[ ， ]

#按索引位置提取区域行数值
#analysis_data.iloc[0:5]

#重设索引
#analysis_data.reset_index()

#设置日期为索引
#analysis_data=analysis_data.set_index('date') 

#使用iloc按位置区域提取数据
##冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列
#analysis_data.iloc[:3,:2]

#适应iloc按位置单独提起数据
#提取第0、2、5行，4、5列
#analysis_data[][]
#analysis_data.iloc[[0,2,5],[4,5]]

#使用ix按索引标签和位置混合提取数据
#2013-01-03号之前，前四列数据
#analysis_data.ix[:'2013-01-03',:4]

#简单的数据采样
#analysis_data.sample(n=3) 

#手动设置采样权重
#weights = [0, 0, 0, 0, 0.5, 0.5]
#analysis_data.sample(n=2, weights=weights) 

#采样后不放回
#analysis_data.sample(n=6, replace=False) 

#采样后放回
#analysis_data.sample(n=6, replace=True)

#数据表描述性统计
#analysis_data.describe().round(2).T #round函数设置显示小数位，T表示转置

# 计算中位数（0到1）
#analysis_data['涨幅'].quantile(0.99)

#计算列的方差
#analysis_data['涨幅'].var()

#计算列的标准差
#analysis_data['涨幅'].std()

#计算两个字段间的协方差
#analysis_data['涨幅'].cov(analysis_data['振幅']) 

#数据表中所有字段间的协方差
#analysis_data.cov()

#两个字段的相关性分析
#相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关
#analysis_data['涨幅'].corr(analysis_data['振幅'])

#数据表的相关性分析
#analysis_data.corr()


#数据表的一阶差分
#analysis_data.diff()

# 计算增长率
# analysis_data['收盘'].pct_change

# 移动窗口函数 xxx：mean corr std min ...
# analysis_data.rolling_xxx()

# 统计图表
# analysis_data.pivot_table()


analysis_data = pd.read_excel('002297.xlsx')
print(analysis_data.shape)
#print(analysis_data.columns)
#选择列
#print(analysis_data.select_dtypes(include=['float']).describe())

#默认移除所有包含空值的行
#dropna(axis=0)
#移除全部为空的值
#analysis_data.dropna(axis=1, how='all')
#移除指定列为空的数据
#analysis_data.dropna(subset=['',])
#设置thresh值移除非None数据个数小于thresh的行
#analysis_data.dropna(thresh=10)


#value_counts

#显示走势图
#analysis_data['开盘'].plot()

#将计算应用于整个数据集
#analysis_data.apply(lambda函数)
#将计算应用于每一个元素
#analysis_data.applymap(lambda函数)


"""
Matplotlib能够的轻易生成直方图，波谱图，条形图，散点图等
"""

import matplotlib.pyplot as plt


data = np.arange(100, 201)

# 横坐标为index，纵坐标为value
#plt.plot(data)
#plt.show()

 
data2 = np.arange(200, 301)

# 创建多个窗口
#plt.figure()
#plt.plot(data2)

#plt.show()


# 同一个窗口显示多个图形
# 参数：矩阵的行数和列数，矩阵的索引。
#plt.subplot(2, 1, 1) # == plt.subplot(211)
#plt.plot(data)


#plt.subplot(2, 1, 2) # == plt.subplot(212)
#plt.plot(data2)

#plt.show()



# 线性图
# 参数：横轴的值，纵轴的值，最后一个参数由两个字符构成的，分别是线条的样式和颜色
# - 直线   : 点线
plt.plot([1, 2, 3], [3, 6, 9], '-r')
plt.plot([1, 2, 3], [2, 4, 9], ':g')

plt.show()


# 散点图
plt.figure()

N = 20
# 参数：c颜色 s大小 alpha透明度
plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='r', s=100, alpha=0.5)
plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='g', s=200, alpha=0.5)
plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='b', s=300, alpha=0.5)

plt.show()

# 饼状图
plt.figure()

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

pie_data = np.random.rand(7) * 100
# autopct指定了数值的精度格式
plt.pie(pie_data, labels=labels, autopct='%1.1f%%')

# 设置了坐标轴大小一致
plt.axis('equal')
# 指明要绘制图例（右上角）
plt.legend()

plt.show()


# 条形图
plt.figure()
N = 7
x = np.arange(N)
bar_data = np.random.randint(low=0, high=100, size=N)
colors = np.random.rand(N * 3).reshape(N, -1)
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.title("Weekday Data")
plt.bar(x, bar_data, alpha=0.8, color=colors, tick_label=labels)
plt.show()

# 直方图
plt.figure()
hist_data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
labels = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]
plt.hist(hist_data, bins=bins, label=labels)

plt.legend()

plt.show()


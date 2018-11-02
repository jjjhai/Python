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
import matplotlib.pyplot as plt
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
analysis_data['开盘'].plot()

#将计算应用于整个数据集
#analysis_data.apply(lambda函数)
#将计算应用于每一个元素
#analysis_data.applymap(lambda函数)





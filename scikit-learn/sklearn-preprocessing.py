# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 10:28:28 2018

@author: Administrator
"""

"""
已处理数据
"""
from sklearn import preprocessing
import numpy as np


#中心化
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
#经过缩放后的数据具有零均值以及标准方差(标准正态分布)
#(x-mean)/std  计算时对每个属性/每列分别进行
X_scaled = preprocessing.scale(X_train)


#默认的中心化会破坏稀疏性，处理稀疏矩阵的时候需要with_mean=False
#保存X_train均值和标准差，在新的数据上实现和训练集相同缩放操作，(x-mean)/std
scaler = preprocessing.StandardScaler().fit(X_train) #StandardScaler(copy=True, with_mean=True, with_std=True)

#均值
scaler.mean_
#缩放比例，同时也是标准差
scaler.scale_
#方差
scaler.var_                                    

scaler.transform(X_train) 

X_test = [[-1., 1., 0.]]

scaler.transform(X_test)




#将特征缩放至特定范围内
#可接受稀疏矩阵

#将简单的数据矩阵缩放到[0, 1]
X_train1 = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])

#preprocessing.minmax_scale
#默认参数feature_range=(0, 1)
min_max_scaler = preprocessing.MinMaxScaler()
#min_max_scaler.fit(X_train1)
#min_max_scaler.transform(X_train1)
X_train_minmax = min_max_scaler.fit_transform(X_train1)

        
print(X_train_minmax)
#缩放比例，(feature_range[1] - feature_range[0]) / X.max(axis=0) - X.min(axis=0)
min_max_scaler.scale_
#移位feature_range[0] - X.min(axis=0) * self.scale_
min_max_scaler.min_
#X_train1未缩放最小值
min_max_scaler.data_min_
min_max_scaler.data_max_
min_max_scaler.data_range_


#实现和训练数据一致的缩放和移位操作
X_test1 = np.array([[ -3., -1.,  4.]])
# X*self.scale_ + self.min_
X_test_minmax = min_max_scaler.transform(X_test1)
X_test_minmax



X_train2 = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])

#通过除以每个特征的最大值将训练数据特征缩放至 [-1, 1] 范围内
#preprocessing.maxabs_scale
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train2)

X_test = np.array([[ -3., -1.,  4.]])
#X / self.scale_
X_test_maxabs = max_abs_scaler.transform(X_test)
#abs(X.max(axis=0))
max_abs_scaler.scale_         
                               

#缩放有离群值的数据
#如果数据包含许多异常值
#不可接受稀疏矩阵
#robust_scale
#RobustScaler 

#核矩阵的中心化
#KernelCenterer

#非线性转换
#提供了一个基于分位数函数的无参数转换，将数据映射到了零到一的均匀分布上
#QuantileTransformer
#quantile_transform
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target
X_train3, X_test3, y_train3, y_test3 = train_test_split(X, y, random_state=0)
quantile_transformer = preprocessing.QuantileTransformer(random_state=0)
X_train_trans = quantile_transformer.fit_transform(X_train3)
X_test_trans = quantile_transformer.transform(X_test3)
np.percentile(X_train3[:, 0], [0, 25, 50, 75, 100]) #array([ 4.3,  5.1,  5.8,  6.5,  7.9])
np.percentile(X_train_trans[:, 0], [0, 25, 50, 75, 100]) #array([ 0.00... ,  0.24...,  0.49...,  0.73...,  0.99... ])




#归一化（区分归一化和缩放区别）
X_train4 = [[ 1., -1.,  2.],
            [ 2.,  0.,  0.],
            [ 0.,  1., -1.]]


#Normalizer（fit方法无效：该类是无状态的，因为该操作独立对待样本）
X_normalized = preprocessing.normalize(X_train4, norm='l2')
print(X_normalized)


#二值化
X_train5 = [[ 1., -1.,  2.],
            [ 2.,  0.,  0.],
            [ 0.,  1., -1.]]

#threshold指定閥值
#preprocessing.binarize
binarizer = preprocessing.Binarizer() #Binarizer(copy=True, threshold=0.0)
binarizer.transform(X_train5)


#分类特征编码
#热编码
#使用m个可能值转换为m值化特征，将分类特征的每个元素转化为一个值
#每列一个特征值，[0,1,2,0]特征值表示有三个类别，所以用100，010，001表示
X_train6 = [[ 0, 0, 3 ],
            [ 1, 1, 0 ],
            [ 0, 2, 1 ],
            [ 1, 0, 2 ]]

#OneHotEncoder(categorical_features='all', dtype=<... 'numpy.float64'>,handle_unknown='error', n_values='auto', sparse=True)
#n_values在类别有缺失的时候显式声明 n_values=[2,3,4]表示每个维度有多少个类别
enc = preprocessing.OneHotEncoder()
enc.fit(X_train6)  
#如果不加toarray()，输出的是稀疏的存储格式，即索引加值的形式
#也可以通过参数指定sparse=False来达到同样的效果
enc.transform([[0, 1, 3]]).toarray() #[[1. 0. 0. 1. 0. 0. 0. 0. 1.]]


#缺失值插补
#Imputer类提供了估算缺失值的基本策略
#使用缺失值所在的行/列中的平均值、中位数或者众数来填充
#这个类也支持不同的缺失值编码
#用平均值补充
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], [np.nan, 3], [7, 6]])
#填充的值：[4,3.666666]
imp.statistics_
X_train7 = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X_train7)) 



#生成多项式特征
#通过增加一些输入数据的非线性特征来增加模型的复杂度
X_train7 = [[0, 1],
            [2, 3],
            [4, 5]]

#interaction_only表示只需要特征间的交互项，为True的时候X_1^2，X_2^2不需要
#PolynomialFeatures(degree=2, interaction_only=False)
poly = preprocessing.PolynomialFeatures(2)
#X的特征从 (X_1, X_2) 转换为 (1, X_1, X_2, X_1^2, X_1X_2, X_2^2) 
poly.fit_transform(X_train7)            


#自定义转换器
#将一个已有的Python函数转化为一个转换器来协助数据清理或处理
#transformer = preprocessing.FunctionTransformer(np.log1p)                                     
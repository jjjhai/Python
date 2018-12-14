# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:09:43 2018

@author: Administrator
"""

from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras import optimizers

import numpy as np

"""
Keras的核心数据结构是model，一种组织网络层的方式
最简单的模型是Sequential顺序模型，它由多个网络层线性堆叠
"""

model = Sequential()

"""
输入参数layers：
时间序列：0 1 2 3 4 5 6 7 8 9 10
输入长度：3天
seq_len=10
[ [0, 1, 2, 3],
  [1, 2, 3, 4],
  [2, 3, 4, 5],
  [3, 4, 5, 6],
  [6, 7, 8, 9],
  [7, 8, 9, 10]
]
x:
[ [0, 1, 2],
  [1, 2, 3],
  [2, 3, 4],
  [3, 4, 5],
  [6, 7, 8],
  [7, 8, 9]
] 
    
y:
[ 3,
  4,
  5,
  6,
  9,
  10
]


"""



seq_len=10
#堆叠模型(LSTM层，Dense层)
#输入数据维度，输出数据维度
model.add(LSTM(input_shape=(None,1),units=seq_len,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(seq_len,return_sequences=False))
model.add(Dropout(0.2)) 
model.add(Dense(input_dim=seq_len,units=1))
model.add(Activation("linear"))
# lr学习效率
rms=optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-06)

"""
编译用来配置模型的学习过程，模型在使用前必须编译，否则在调用fit或evaluate时会抛出异常
loss：损失函数，可用mse,mae,binary_crossentropy等
optimizers：优化器，即优化参数的算法，可供选择为SGD（随机梯度下降法），RMSprop（处理递归神经网络时的一个良好选择），Adagrad等（具体参见http://keras-cn.readthedocs.io/en/latest/ ，网页提供Keras相关函数的详细介绍）

"""
model.compile(loss="mse", optimizer=rms)

#训练数据（LSTM神经网络接受的input为3维数组）
#nb_epoch：迭代次数
#validation_split：0~1之间的浮点数，用来指定训练集的一定比例数据作为验证集
#model.fit(X_train,y_train,batch_size=conf.batch,nb_epoch=conf.epochs,validation_split=conf.validation_split)

#将批次的数据提供给模型
#model.train_on_batch(x_batch, y_batch)

#评估模型性能
#loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# 对新的数据生成预测
#classes = model.predict(x_test, batch_size=128)




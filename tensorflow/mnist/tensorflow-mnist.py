# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:44:01 2018

@author: Administrator
"""

import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf




x = tf.placeholder("float", [None, 784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)


# 计算成本函数：交叉熵
# 计算损失
y_ = tf.placeholder("float", [None,10])
#累加( 实际值*log(预测值) )
cross_entropy = -tf.reduce_sum(y_*tf.log(y))


train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)


init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# 随机梯度下降训练
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  print(sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y_: batch_ys}))


# argmax找最大值，参数二为纬度，在第二纬度
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# cast类型转换
# reduce_mean求平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

sess.close()

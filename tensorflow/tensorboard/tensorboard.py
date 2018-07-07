# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:48:10 2018

@author: Administrator
"""

"""
TensorBoard可以将训练过程中的各种绘制数据展示出来
包括标量（scalars），图片（images），音频（Audio）,计算图（graph）,数据分布，直方图（histograms）和嵌入式向量

summary_op（汇总节点）包括了summary.scalar、summary.histogram、summary.image等操作
这些操作输出的是各种summary protobuf，最后通过summary.writer写入到event文件（事件文件）中

tf.train.Summarywriter/tf.summary.FileWriter：写入序列化的Summary protobuf对象

使用tf.summary.merge合并汇总
使用tf.summary.merge_all/tf.merge_all_summaries合并默认图形中的所有汇总
"""

"""
TensorFlow 图表有两种连接关系：数据依赖和控制依赖
数据依赖显示两个操作之间的tensor流程，用实心箭头指示
控制依赖用虚线表示
"""




import tensorflow as tf

tf.reset_default_graph()

#a = tf.constant([1.0,2.0,3.0],name='input1')
#b = tf.Variable(tf.random_uniform([3]),name='input2')
#add = tf.add_n([a,b],name='addOP')
#with tf.Session() as sess:
#    sess.run(tf.global_variables_initializer())
#    writer = tf.summary.FileWriter("train/",sess.graph)
#    print(sess.run(add))
#writer.close()



# 添加命名空间，会以input1/变量名 形式保存
with tf.variable_scope('input1'):
    input1 = tf.constant([1.0,2.0,3.0],name='input1')
with tf.variable_scope('input2'):
    input2 = tf.Variable(tf.random_uniform([3]),name='input2')
add = tf.add_n([input1,input2],name='addOP')
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
#    汇总数据：数据序列化
    writer = tf.summary.FileWriter("train/",sess.graph)
    print(sess.run(add))
writer.close()


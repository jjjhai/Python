# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:52:34 2018

@author: Administrator
"""

import tensorflow as tf

# 新建一个 graph.
# 手工指派设备
# with tf.device('/cpu:0'):
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    
c = tf.matmul(a, b)

# log_device_placement设置为True：记录设备指派情况
# allow_soft_placement设置为True：自动选择一个存在并且支持的设备来运行operation
with tf.Session(config=tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)) as sess:  
    # 运行这个 op.
    print(sess.run(c))
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:12:09 2018

@author: Administrator
"""

import tensorflow as tf


labels = tf.constant([0,2,3,6,7,9])
labels = tf.expand_dims(labels, 1)
indices = tf.expand_dims(tf.range(0, 6, 1), 1)
concated = tf.concat([indices, labels], 1)
onehot_labels = tf.sparse_to_dense(concated, tf.stack([6, 10]), 1.0, 0.0)

with tf.Session() as sess:
    a = sess.run(labels)
    b = sess.run(indices)
    c = sess.run(concated)
    
    d = sess.run(onehot_labels)
    
    e = sess.run(onehot_labels)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:15:15 2018

@author: Administrator
"""

import tensorflow as tf


tf.reset_default_graph()
 
  
#module_file =  tf.train.latest_checkpoint('tmp/')
##module_file = tf.train.latest_checkpoint("tmp")
#with tf.Session() as sess:
#    
#    sess.run(tf.global_variables_initializer())
#    if module_file is not None:
#        saver.restore(sess, module_file)
# 
#sess.close()


weights = tf.Variable(tf.zeros([784, 200]), name="weights")
w2 = tf.Variable(tf.zeros([784, 200]), name="w2")
w_twice = tf.Variable(tf.zeros([784, 200]), name="w_twice")

biases = tf.Variable(tf.zeros([200]), name="biases")


# 给graph的所有变量，或是定义在列表里的变量添加save和restore ops
saver = tf.train.Saver()
#{'weights_rename': weights, 'w2': w2, 'w_twice': w_twice, 'biases':biases}

# 添加一个op来初始化模型的所有变量
init_op = tf.global_variables_initializer()


# Later, when launching the model
with tf.Session() as sess:
  # Run the init operation.
  sess.run(init_op)
  
  print(sess.run(weights))
  
  module_file =  tf.train.latest_checkpoint('tmp/')
  saver.restore(sess, module_file)
  
  all_vars = tf.trainable_variables()
  for v in all_vars:
    print(v.name)
  
  print(sess.run(weights))
  

  
sess.close()
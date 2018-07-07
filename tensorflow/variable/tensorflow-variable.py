# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:53:10 2018

@author: Administrator
"""

import tensorflow as tf

"""
tf.global_variables_initializer()把Variable初始化为全局变量， 写在graph上，需要清除graph才能清除变量
"""
tf.reset_default_graph()

# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35), name="weights")
# 由另一个变量初始化
# Create another variable with the same value as 'weights'.
w2 = tf.Variable(weights.initialized_value(), name="w2")
# Create another variable with twice the value of 'weights'
w_twice = tf.Variable(weights.initialized_value() * 0.2, name="w_twice")

biases = tf.Variable(tf.zeros([200]), name="biases")


# 给graph的所有变量，或是定义在列表里的变量添加save和restore ops
saver = tf.train.Saver()
# 存储的时候重新命名, 前面是命名，后面是变量
#{'weights_rename': weights, 'w2': w2, 'w_twice': w_twice, 'biases':biases}

# 添加一个op来初始化模型的所有变量
init_op = tf.global_variables_initializer()


# Later, when launching the model
with tf.Session() as sess:
  # Run the init operation.
  sess.run(init_op)
  
#  sess.run(weights)
#  sess.run(w2)
#  sess.run(w_twice)
#  sess.run(biases)
  
  #tf.trainable_variables () 指的是需要训练的变量 
  #tf.all_variables() 指的是所有变量
  all_vars = tf.trainable_variables()
  for v in all_vars:
    print(v.name)
  
   # Save the variables to disk.
  save_path = saver.save(sess, "tmp/model.ckpt")
  print("Model saved in file: ", save_path)
  
#  saver.restore(sess, "tmp/model.ckpt")
  
sess.close()
  
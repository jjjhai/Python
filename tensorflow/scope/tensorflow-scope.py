# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:24:52 2018

@author: Administrator
"""

import tensorflow as tf

tf.reset_default_graph()


"""
tf.get_variable(<name>, <shape>, <initializer>): 通过所给的名字创建或是返回一个变量
tf.variable_scope(<scope_name>): 通过tf.get_variable()为变量名指定命名空间
"""

"""
是否允许共享变量：tf.get_variable_scope().reuse
false: 全称变量已经存在会报错
true: 全称变量不存在会报错

三种方法修改：
1.
with tf.variable_scope("xxx") as scope:
    scope.reuse_variables()
    
2.
with tf.variable_scope("xxx", reuse=True) as scope:   
    
3.
with tf.variable_scope("xxx"):
    tf.get_variable_scope().reuse_variables()
    
"""


"""
print(tf.get_variable_scope().reuse)


def getvariable():
    with tf.variable_scope("conv1"):
        # tf.constant_initializer(value) 初始化一切所提供的值
        # tf.random_uniform_initializer(a, b) 从a到b均匀初始化
        # tf.random_normal_initializer(mean, stddev) 用所给平均值和标准差初始化均匀分布
        biases  = tf.get_variable("biases", shape=[32], initializer=tf.random_normal_initializer())
    

    with tf.variable_scope("conv2"):
        biases  = tf.get_variable("biases", shape=[32], initializer=tf.random_normal_initializer())

with tf.variable_scope("conv_share") as scope:
    getvariable()
    # 检索当前变量作用域（tf.get_variable_scope().reuse_variables()）
    print(tf.get_variable_scope())
    # 共享变量
    scope.reuse_variables()
    getvariable()

with tf.Session() as sess:
  
  all_vars = tf.trainable_variables()
  for v in all_vars:
    print(v.name)

"""

# 变量作用域的继承与独立性

"""
with tf.variable_scope("root"):
    print(tf.get_variable_scope().reuse) # False
    with tf.variable_scope("foo"):
        print(tf.get_variable_scope().reuse) # False
    with tf.variable_scope("foo", reuse=True):
        print(tf.get_variable_scope().reuse) # True
        with tf.variable_scope("bar"):
            print(tf.get_variable_scope().reuse) # True

    print(tf.get_variable_scope().reuse) # False
"""  

# 获取变量作用域
"""
with tf.variable_scope("foo") as foo_scope:
    print(foo_scope.name) # foo
with tf.variable_scope("bar"):
    with tf.variable_scope("baz") as other_scope:
        print(other_scope.name) # bar/baz
        with tf.variable_scope(foo_scope) as foo_scope2:
            print(foo_scope2.name) # foo
"""            


# 默认初始化器
"""
with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
    v = tf.get_variable("v", [1]) # 0.4
    w = tf.get_variable("w", [1], initializer=tf.constant_initializer(0.3)) # 0.3
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1]) # 0.4
        with tf.variable_scope("baz", initializer=tf.constant_initializer(0.2)):
            v = tf.get_variable("v", [1]) # 0.2
"""

# 名称作用域
with tf.variable_scope("foo"):
    with tf.name_scope("bar"):
        v = tf.get_variable("v", [1]) # v.name == "foo/v:0"
        x = 1.0 + v # x.op.name == "foo/bar/add"



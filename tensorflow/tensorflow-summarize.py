# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:06:48 2018

@author: Administrator
"""

"""
使用图 (graph) 来表示计算任务.
图中的节点被称之为 op (operation 的缩写). 一个 op 获得 0 个或多个 Tensor, 执行计算, 产生 0 个或多个 Tensor. 


在会话 (Session) 的上下文 (context) 中执行图.
会话将图的 op 分发到诸如 CPU 或 GPU 之类的设备上, 同时提供执行 op 的方法. 这些方法执行后, 将产生的 tensor 返回.

使用 tensor 表示数据.
每个 tensor 是一个类型化的多维数组.一个 tensor 包含一个静态类型 rank, 和 一个 shape. 

通过 变量 (Variable) 维护状态.

使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.
"""

"""
TensorFlow 程序通常被组织成一个构建阶段和一个执行阶段. 
构建阶段：op 的执行步骤被描述成一个图.
执行阶段：使用会话执行图中的 op.

通常在构建阶段创建一个图来表示和训练神经网络, 然后在执行阶段反复执行图中的训练 op.
"""

"""
构建图
创建源 op (source op). 源 op 不需要任何输入, 例如常量 (Constant). 源 op 的输出被传递给其它 op 做运算.
"""

import tensorflow as tf

# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])

# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)

"""
在会话中启动图
"""
# 启动默认图.
sess = tf.Session()

# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# 
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print(result)

# 任务完成, 关闭会话.
sess.close()

"""
变量
"""
# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0, name="counter")

# 创建一个 op, 其作用是使 state 增加 1
one = tf.constant(1)
new_value = tf.add(state, one)
# 将 new_value 更新到 state
update = tf.assign(state, new_value)


# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.global_variables_initializer()

# 启动图, 运行 op
with tf.Session() as sess:
  # 运行 'init' op
  sess.run(init_op)
  # 打印 'state' 的初始值
  print(sess.run(state))
  # 运行 op, 更新 'state', 并打印 'state'
  for _ in range(3):
    sess.run(update)
    print(sess.run(state))


"""
Fetch：取回多个 tensor
"""
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print(result)



"""
Feed：临时替代图中的任意操作中的 tensor 可以对图中任何操作提交补丁, 直接插入一个 tensor.
"""
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
  print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:16:15 2018

@author: Administrator
"""

"""
数据读取
供给数据(Feeding)： 在TensorFlow程序运行的每一步， 让Python代码来供给数据（feed_dict）
从文件读取数据： 在TensorFlow图的起始， 让一个输入管线从文件中读取数据
预加载数据： 在TensorFlow图中定义常量或变量来保存所有数据(仅适用于数据量比较小的情况)
"""

import tensorflow as tf

import numpy as np 

#tf.reset_default_graph()

directory = "*.csv"
# 产生文件名列表
file_names = tf.train.match_filenames_once(directory)


# 生成一个先入先出的队列，文件阅读器会需要它来读取数据
# 参数：shuffle是否乱序   num_epochs最大的训练迭代数（每个文件读多少次）
filename_queue = tf.train.string_input_producer(file_names, num_epochs=2)


# 文件阅读器（在一个文件队列上操作，从队列中取出一个文件名，读取完这个文件里内容后又取出另一个文件名直到文件队列为空）
# 队列最开始是空的，队列的填充是通过QueueRunners来实现的（将文件名推入到文件名队列）
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# 使用tf.FixedLengthRecordReader tf.decode_raw从二进制文件中读取固定长度纪录
# 使用tf.TFRecordReader tf.parse_single_example读取TFRecords文件
"""
TFRecords文件
二进制文件，将协议内存块（protocal buffer）序列化为一个字符串写入到文件，可以统一不同输入文件
步骤：
1.建立TFRecord存储器：tf.python_io.TFRecordWriter（写入到TFRecords文件）
2.构造每个样本的Example模块：tf.train.Example（协议内存块，包含字段Features）
"""

record_defaults = [[1.0], [1.0], [1.0], [1.0], [1.0], [1]] # 这里的数据类型决定了读取的数据类型，而且必须是list形式

# decode_csv解析这一行内容并将其转为张量列表
col1, col2, col3, col4, col5, col6 = tf.decode_csv(value, record_defaults=record_defaults)

# tf.train.batch([example, label], batch_size=batch_size, capacity=capacity)：按顺序组合成一个batch：capacity是队列中的容量
# tf.train.shuffle_batch对队列中的样本进行乱序处理：min_after_dequeue必须小于capacity
# tf.train.shuffle_batch_join(example_list, batch_size=batch_size, capacity=capacity,min_after_dequeue=min_after_dequeue)有更强的乱序和并行处理
"""
可以使用tf.train.slice_input_producer作切片处理，让样本在整个迭代中被打乱
tf.train.batch与tf.train.shuffle_batch函数是单个Reader读取，可以多线程（同一时刻只在一个文件中进行读取操作）
tf.train.batch_join与tf.train.shuffle_batch_join可设置多Reader读取，每个Reader使用一个线程
"""
#exampleBatch, labelBatch = tf.train.shuffle_batch([example, label], batch_size = batchSize, num_threads = 3, capacity = capacity, min_after_dequeue = min_after_dequeue)  


 
init = (tf.global_variables_initializer(), tf.local_variables_initializer())


with tf.Session() as sess:
    
    sess.run(init)
    
    coord = tf.train.Coordinator()  
    
    # 启动输入管道的线程，填充文件名到队列中（QueueRunner类）
    threads = tf.train.start_queue_runners(coord=coord)  

    
    
    try:
        while not coord.should_stop():
            a, b, c, x, y, z, _key = sess.run([col1, col2, col3, col4, col5, col6, key])
            print("%f, %f, %f, %f, %f, %d, key:%s" % (a, b, c, x, y, z, _key))
            
        
    except tf.errors.OutOfRangeError:  
        print('Done reading')  

    finally:  
        coord.request_stop()  
        
    coord.join(threads) 
    sess.close()
    

"""
在数据流图建立后初始化变量
"""

"""

training_data = np.random.rand(4,3)

with tf.Session() as sess:
    
    data_initializer = tf.placeholder(dtype=training_data.dtype,shape=training_data.shape)
    
    # trainable=False可以防止该变量被数据流图的 GraphKeys.TRAINABLE_VARIABLES 收集，这样就不会在训练的时候尝试更新它的值
    # collections=[]可以防止GraphKeys.VARIABLES收集后作为保存和恢复的中断点
    input_data = tf.Variable(data_initializer, trainable=False, collections=[])
    
    sess.run(input_data.initializer,feed_dict={data_initializer: training_data})
    
    print(sess.run(input_data))

"""
    

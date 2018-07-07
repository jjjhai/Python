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

#tf.reset_default_graph()

directory = "*.csv"
# 产生文件名列表
file_names = tf.train.match_filenames_once(directory)


# 生成一个先入先出的队列，文件阅读器会需要它来读取数据
filename_queue = tf.train.string_input_producer(file_names, num_epochs=1)


# 文件阅读器（在一个文件队列上操作，从队列中取出一个文件名，读取完这个文件里内容到队列后又取出另一个文件名直到文件队列为空
# 队列最开始是空的，队列的填充是通过QueueRunners来实现的
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

record_defaults = [[1.0], [1.0], [1.0], [1.0], [1.0], [1]] # 这里的数据类型决定了读取的数据类型，而且必须是list形式
col1, col2, col3, col4, col5, col6 = tf.decode_csv(value, record_defaults=record_defaults) # 解析出的每一个属性都是rank为0的标量



#exampleBatch, labelBatch = tf.train.shuffle_batch([example, label], batch_size = batchSize, num_threads = 3, capacity = cap acity, min_after_dequeue = min_after_dequeue)  


 
init = (tf.global_variables_initializer(), tf.local_variables_initializer())

 
with tf.Session() as sess:
    
    sess.run(init)
    
    coord = tf.train.Coordinator()  
    
    # 启动输入管道的线程，填充样本到队列中（QueueRunner类）
    threads = tf.train.start_queue_runners(coord=coord)  

    # Retrieve a single instance:try:#while not coord.should_stop():
    
    
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

    

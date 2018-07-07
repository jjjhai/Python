# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:17:23 2018

@author: Administrator
"""
"""
队列是TensorFlow图中的节点，是一种有状态的节点，就像变量一样：其他节点可以修改它的内容
其他节点可以把新元素插入到队列后端(rear)，也可以把队列前端(front)的元素删除

"""
import tensorflow as tf

import threading
import numpy as np


"""
Coordinator类用来帮助多个线程协同工作，多个线程同步终止，可以向那个在等待所有工作线程终止的程序报告异常
"""

"""
# 线程体：循环执行，直到Coordinator收到了停止请求
def MyLoop(coord, index):
    i = 0
    # 如果线程应该停止则should_stop返回True
    while not coord.should_stop():
        i += 1
        print("%d:%d" % (index,i))

        if i > 10000:
            # request_stop会去停止其他线程
            print("%drequest_stop" % (index))
            coord.request_stop()

# Main code: create a coordinator.
coord = tf.train.Coordinator()

# Create 10 threads that run 'MyLoop()'
threads = [threading.Thread(target=MyLoop, args=(coord,i)) for i in range(2)]

# Start the threads and wait for all of them to stop.
for t in threads: t.start()
# 等待被指定的线程终止
coord.join(threads)
"""


"""
tf.FIFOQueue 按入列顺序出列的队列
tf.RandomShuffleQueue 随机顺序出列的队列
tf.PaddingFIFOQueue 以固定长度批量出列的队列
tf.PriorityQueue 带优先级出列的队列
"""

"""
#创建的图:一个先入先出队列
q = tf.FIFOQueue(3, "float")  
init = q.enqueue_many(([0.1, 0.2, 0.3],))  #一次往队列中输入多个值

queue = tf.RandomShuffleQueue(3, "float")
enqueue_op = queue.enqueue([0.1, 0.2, 0.3])

x = q.dequeue()  #从队列中取出一个值
y = x + 1  
q_inc = q.enqueue([y])  #往队列中push一个值

# 开启一个session，session是会话,会话的潜在含义是状态保持，各种tensor的状态保持  
with tf.Session() as sess:  
    sess.run(init)  
    
    for i in range(2):  
        sess.run(q_inc)  
        
    quelen =  sess.run(q.size())  
    for i in range(quelen):  
        print (sess.run(q.dequeue())) 
"""        




"""
QueueRunner类用来协调多个工作线程同时将多个张量推入同一个队列中
QueueRunner类会创建一组线程， 这些线程可以重复的执行Enquene操作
"""

"""
q = tf.FIFOQueue(10, "float")  
counter = tf.Variable(0.0)  #计数器
# 给计数器加一
increment_op = tf.assign_add(counter, 1.0)
# 将计数器加入队列
enqueue_op = q.enqueue(counter)

# 创建QueueRunner
# 用多个线程向队列添加数据
# 这里实际创建了4个线程，两个增加计数，两个执行入队
qr = tf.train.QueueRunner(q, enqueue_ops=[increment_op, enqueue_op] * 2)


with tf.Session() as sess:  
    sess.run(tf.global_variables_initializer())  
    

    # 启动入队线程
    qr.create_threads(sess, start=True)
    for i in range(200):
        print (sess.run(q.dequeue()))

"""


# QueueRunner和Coordinator一起使用

# 1000个4维输入向量，每个数取值为1-10之间的随机数
data = 10 * np.random.randn(1000, 4) + 1
# 1000个随机的目标值，值为0或1
target = np.random.randint(0, 2, size=1000)

# 创建Queue，队列中每一项包含一个输入数据和相应的目标值
queue = tf.FIFOQueue(capacity=50, dtypes=[tf.float32, tf.int32], shapes=[[4], []])

# 批量入列数据（这是一个Operation）
enqueue_op = queue.enqueue_many([data, target])
# 出列数据（这是一个Tensor定义）
data_sample, label_sample = queue.dequeue()

# 创建包含4个线程的QueueRunner
qr = tf.train.QueueRunner(queue, [enqueue_op] * 4)

with tf.Session() as sess:
    # 创建Coordinator
    coord = tf.train.Coordinator()
    # 启动QueueRunner管理的线程
    enqueue_threads = qr.create_threads(sess, coord=coord, start=True)
    # 主线程，消费100个数据
    for step in range(100):
        if coord.should_stop():
            break
        data_batch, label_batch = sess.run([data_sample, label_sample])
        print(step)
    # 主线程计算完成，停止所有采集数据的进程
    coord.request_stop()
    coord.join(enqueue_threads)




        






        

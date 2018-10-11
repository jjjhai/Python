# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:59:50 2018

@author: Administrator
"""

from datetime import datetime
import time as ts

month = "Jun"
day = "19"
time = "22:43:03"

#strptime将一个日期字符串转成datetime日期格式便于后期处理
str_time = str(datetime.strptime(month+day.zfill(2)+time+str(datetime.now().year), "%b%d%X%Y"))

print(str_time)

print(datetime.now().strftime('%Y-%b-%d %H:%M:%S'))

print(ts.strftime('%Y-%m-%d %H:%M:%S', ts.localtime(1347517370)))
print(ts.strftime('%Y-%m-%d %H:%M:%S', ts.gmtime(134611471792/1000.)))


ts_epoch = 1362301382   
dt = datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')   
print(dt)  


start = ts.time()
print('Done! Elapsed %d seconds.\n' % (ts.time() - start, ))

#将一个以struct_time格式转换为时间戳
print(ts.mktime(ts.localtime()))

ts.sleep(1)

print(ts.clock())






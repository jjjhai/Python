# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:23:36 2018

@author: Administrator
"""

from urllib import request,parse  
from urllib.error import URLError  
import threading

import time
from http import client

HOST = "120.76.203.123"
PORT = 85
URL = "/TjsAppDcOrder/CreateDcOrder"
TOTAL = 0
SUCC = 0
FAIL = 0
EXCEPT = 0
MAXTIME = 0
MINTIME = 100
GT3 = 0
LT3 = 0


"""
data = parse.urlencode({'Id': 0, 
                        'OrderSn': 0,
						'SupplierId': 1,
						'LocationId': 1,
						'OrderStatus': 0,
						'ConfirmStatus': 0,
						'PayStatus': 0,
						'TotalPrice': 0,
						'MenuPrice': 0,
						'PackagePrice': 0,
						'DeliveryPrice': 0,
						'PayAmount': 0,
						'PayTime': 0,
						'AccountMoney': 0,
						'OrderMenu': '[{"Id":1,"Name":"鸡腿堡","CateId":1,"Price":0.01,"Image":"http://192.168.3.22/Images/Menus/1/1.jpg","Tags":"","IsEffect":1,"LocationId":1,"SupplierId":1,"BuyCount":1,"XPoint":"114.038167","YPoint":"22.673962","DcMenuCateType":1,"OpenTimeCfgStr":"","Enabled":0,"User":"","Time":"2017-01-01 10:10:00","OrgId":0}]',
						'UserId': 4,
						'XPoint': 0,
						'YPoint': 0,
						'Address': '',
						'ApiAddress': '',
						'Consignee': '',
						'Mobile': 0,
						'DcComment': 0,
						'LocationName': ''}) 
try:
    conn = client.HTTPConnection(HOST, PORT)    
    conn.request('POST', URL, data)  
    res = conn.getresponse()
    print(bytes.decode(res.read()))
except Exception as e:  
    print(e)  
    
"""

class RequestThread(threading.Thread):  
    # 构造函数  
    def __init__(self, thread_name, data):  
        threading.Thread.__init__(self)  
        self.test_count = 0
        self.data = data
  
    # 线程运行的入口函数  
    def run(self):  
        self.test_performace()  
  
  
    def test_performace(self):  
            global TOTAL  
            global SUCC  
            global FAIL  
            global EXCEPT  
            global GT3  
            global LT3  
            try:  
                st = time.time()
                conn = client.HTTPConnection(HOST, PORT)    
                conn.request('POST', URL, self.data)  
                res = conn.getresponse()
                #print(bytes.decode(res.read()))
                #print('version:', res.version)    
                #print('reason:', res.reason)    
                #print('status:', res.status)   
                #print('msg:', res.msg)    
                #print('headers:', res.getheaders())  
                if res.status == 200:  
                    TOTAL+=1  
                    SUCC+=1  
                else:  
                    TOTAL+=1  
                    FAIL+=1  
                time_span = time.time()-st  
                #print('%s:%f\n'%(self.name,time_span))  
                self.maxtime(time_span)  
                self.mintime(time_span)  
                if time_span>3:  
                    GT3+=1  
                else:  
                    LT3+=1                      
            except Exception as e:  
                #print(e)  
                TOTAL+=1  
                EXCEPT+=1  
            conn.close()
            
    def maxtime(self,ts):  
            global MAXTIME  
            #print(ts)  
            if ts>MAXTIME:  
                MAXTIME=ts  
    def mintime(self,ts):  
            global MINTIME  
            if ts<MINTIME:  
                MINTIME=ts  

# main 代码开始  
print('===========task start===========')  
# 开始的时间  
start_time = time.time()  
# 并发的线程数  
thread_count = 300 
  
i = 1 
                        
                        
data = parse.urlencode({
                        'OrderSn': 0,
						'SupplierId': 1,
						'LocationId': 1,
						'OrderStatus': 0,
						'ConfirmStatus': 0,
						'PayStatus': 0,
						'TotalPrice': 0,
						'MenuPrice': 0,
						'PackagePrice': 0,
						'DeliveryPrice': 0,
						'PayAmount': 0,
						'PayTime': 0,
						'AccountMoney': 0,
						'OrderMenu': '[{"Id":1,"Name":"鸡腿堡","CateId":1,"Price":0.01,"Image":"http://192.168.3.22/Images/Menus/1/1.jpg","Tags":"","IsEffect":1,"LocationId":1,"SupplierId":1,"BuyCount":1,"XPoint":"114.038167","YPoint":"22.673962","DcMenuCateType":1,"OpenTimeCfgStr":"","Enabled":0,"User":"","Time":"2017-01-01 10:10:00","OrgId":0}]',
						'UserId': 4,
						'XPoint': 0,
						'YPoint': 0,
						'Address': '',
						'ApiAddress': '',
						'Consignee': '',
						'Mobile': 0,
						'DcComment': 0,
						'LocationName': ''})

packageData = parse.urlencode({
                        'OrderSn': 0,
						'SupplierId': 1,
						'LocationId': 1,
						'OrderStatus': 0,
						'ConfirmStatus': 0,
						'PayStatus': 0,
						'TotalPrice': 0,
						'MenuPrice': 0,
						'PackagePrice': 0,
						'DeliveryPrice': 0,
						'PayAmount': 0,
						'PayTime': 0,
						'AccountMoney': 0,
						'OrderMenu': '[{"Id":1,"Name":"鸡腿堡","CateId":1,"Price":0.01,"Image":"http://192.168.3.22/Images/Menus/1/1.jpg","Tags":"","IsEffect":1,"LocationId":1,"SupplierId":1,"BuyCount":1,"XPoint":"114.038167","YPoint":"22.673962","DcMenuCateType":1,"OpenTimeCfgStr":"","Enabled":0,"User":"","Time":"2017-01-01 10:10:00","OrgId":0}]',
						'UserId': 4,
						'XPoint': 0,
						'YPoint': 0,
						'Address': '',
						'ApiAddress': '',
						'Consignee': '',
						'Mobile': 0,
						'DcComment': 0,
						'LocationName': ''})
while i <= thread_count:  
    t = RequestThread("thread" + str(i), data)  
    t.start()  
    i += 1  
t=0  
#并发数所有都完成或大于50秒就结束  
#TOTAL<thread_count and
while t<1:  
        #print("total:%d,succ:%d,fail:%d,except:%d\n"%(TOTAL,SUCC,FAIL,EXCEPT))
        t+=1  
        time.sleep(0.9)  
print('===========task end===========')
print('花费时间:%d秒'% (t,))  
print("处理总数:%d,成功:%d,失败:%d,报错:%d"%(TOTAL,SUCC,FAIL,EXCEPT))  
print('响应最长时间:',MAXTIME)  
print('响应最短时间',MINTIME)  
print('大于3秒的占比:%d,百分比:%0.2f'%(GT3,float(GT3)/TOTAL))  
print('小于3秒的占比:%d,百分比:%0.2f'%(LT3,float(LT3)/TOTAL))  

























"""
class postRequest():  
    def __init__(self,url,values,interface_name):  
        self.url = url  
        self.values = values  
        self.interface_name = interface_name  
          
    def post(self):  
        parms=self.values  
        querystring = parse.urlencode(parms)  
        try:  
            u = request.urlopen(self.url,querystring.encode('ascii'))  
            resp = u.read()  
            print("接口名字为：",self.interface_name)  
            print("所传递的参数为：\n",parms)  
            print("服务器返回值为：\n",resp)  
        except URLError as e:  
            print (e)
            

def Login():                        #定义接口函数  
    #实例化接口对象  
    login  = postRequest('http://120.76.203.123:85/TjsDeviceVideo/LoadAll',{},"Tjs")  
    login.post()  


try:  
    i = 0  
    tasks = []                                      #任务列表  
    task_number = 2000 
    while i < task_number:  
        t = threading.Thread(target=Login)    
        #tasks.append(t)                             #加入线程池，按需使用  
        t.start()                   #多线程并发 
        i = i + 1
except Exception as e:  
    print (e)  
"""


    


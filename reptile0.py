# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:53:45 2018

@author: Administrator
"""

from urllib import request
from bs4 import BeautifulSoup

import re

resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/shenzhen/')
html_data = resp.read().decode('utf-8')


soup = BeautifulSoup(html_data, 'html.parser')

nowplaying_movie = soup.find_all('div', id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    for tag_img_item in item.find_all('img'):
        nowplaying_dict['name'] = tag_img_item['alt']            
        nowplaying_list.append(nowplaying_dict) 
    

#print(nowplaying_list)

requrl = 'https://movie.douban.com/subject/' + nowplaying_list[0]['id'] + '/comments' +'?' +'start=0' + '&limit=20'
resp = request.urlopen(requrl)
html_data = resp.read().decode('utf-8') 
soup = BeautifulSoup(html_data, 'html.parser') 
comment_div_lits = soup.find_all('div', class_='comment') 

eachCommentList = []; 
for item in comment_div_lits: 
    if item.find_all('p')[0].string is not None:
        eachCommentList.append(item.find_all('p')[0].string)

#print(eachCommentList)



comments = ''
for k in range(len(eachCommentList)):
    comments = comments + (str(eachCommentList[k])).strip()



pattern = re.compile(r'[u4e00-u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)









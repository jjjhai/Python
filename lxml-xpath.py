# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:33:59 2018

@author: Administrator
"""

from lxml import etree

text = '''   
<div>   
    <ul>   
         <li class="item-0"><a href="link1.html">first item</a></li>   
         <li class="item-1"><a href="link2.html">second item</a></li>   
         <li class="item-inactive"><a href="link3.html">third item</a></li>   
         <li class="item-1"><a href="link4.html">fourth item</a></li>   
         <li class="item-0"><a href="link5.html">fifth item</a>   
         <br>   
     </ul>   
 </div>   
'''   
#具有自动修正HTML代码的功能
html = etree.HTML(text)   
result = etree.tostring(html)   
print(result)

#直接从文件读取
html_file = etree.parse('test.html')   
result_file = etree.tostring(html_file)   
print(result_file)

#XPath是一门在XML文档中查找信息的语言
html_path = etree.HTML(text)   
result_path = html_path.xpath('//li/a/text()')   
print(result_path)
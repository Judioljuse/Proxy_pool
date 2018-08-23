# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:55:46 2018

@author: 郑宗
"""

import requests  

# 代理IP
proxies = '103.232.33.6:21231'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'https://book.douban.com/'  
# proxies是requests中的代理 choice是随机使用一个IP 这里http 和 https最好都写上
response = requests.get(url, proxies={'http': proxies,'https':proxies}, headers=head) 

# 输出代理IP
print(response.text)  
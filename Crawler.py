# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:21:12 2018

@author: 郑宗
"""

#from .utils import get_page
from pyquery import PyQuery as pq

import urllib.request
def get_page(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    except Exception as e:
        return 'Url Error'

class ProxyMetaclass(type):
    def __new__(cls,name,bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count +=1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases ,attrs)
    
class Crawler(object, metaclass=ProxyMetaclass):
                        
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print("成功获取到代理",proxy)
            proxies.append(proxy)
        return proxies
    
    def crawl_daili66(self ,page_count=10):
        '''
        获取代理66
        :param page_count: 页码
        :return: 代理
        '''
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1,page_count +1)]
        for url in urls:
            print('Crawling',url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])
        
    def crawl_proxy360(self):
        '''
        获取代理 Proxy360
        return: 代理
        '''
        start_url = 'http://www.proxy360.cn/Region/China'
        print('Crawling',start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            lines = doc('div[name="list_proxy_ip"]').items()
            for line in lines:
                ip = line.find('.tbBottomLine:nth-child(1)').text()
                port = line.find('.tbBottomLine:nth-child(2)').text()
                yield ':'.join([ip,port])
            
    
    def crawl_goubanjia(self):
        '''
        获取 Goubanjia
        :return: 代理
        '''
        start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
        print('Crawling',start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace(' ','')
            
        

        
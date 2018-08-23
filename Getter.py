# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:26:28 2018

@author: 郑宗
"""

from db import RedisClient
from Crawler import Crawler

from config import POOL_UPPER_THRESHOLD

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        '''
        判断是否达到了代理池限制
        '''
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
                    
import requests
import json
def getCountry(ipAddress,access_key='2a6b7df0691cc4bc9883b87eeb8f1030'):
    try:
        response = requests.get("http://api.ipstack.com/{}?access_key={}".format(ipAddress,access_key))
    except:
        return None
    responseJson = json.loads(response.text)
    return responseJson
    
                    
                    
def find(word,letter):
        """
        寻址函数
        :return: 下标
        """
        index=0
        while index<len(word):
            if word[index:index+len(letter)]==letter:
                return index
            index=index+1
        return -1 
                    
                    
                    
                    
                
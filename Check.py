# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:29:35 2018

@author: 郑宗
"""
import aiohttp
import asyncio
import time

from error import ClientError,ClientConnectorError
from db import RedisClient

from config import VALID_STATUS_CODES
from config import TEST_URL
from config import BATCH_TEST_SIZE

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()
        
    async def test_single_proxy(self,proxy):
        '''
        测试单个代理
        :param: proxy: 单个代理
        :return: None
        '''
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' +proxy
                print('正在测试',proxy)
                async with session.get(TEST_URL ,proxy=real_proxy,timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求码响应不合法',proxy)
            except:
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)
            
    
    def run(self):
        '''
        请求主函数
        '''
        print('测试器开始运行')
        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop()
            #批量测试
            for i in range(0,len(proxies),BATCH_TEST_SIZE):
                test_proxies = proxies[i:i + BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误',e.args)
                    
                    
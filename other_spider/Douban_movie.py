import json
import urllib.request
from flask import flash


movie_type={'剧情': 11,'喜剧': 24,'动作':5,'爱情':13,'科幻':17,'动画':25,'悬疑':10,'惊悚':19,'恐怖':20,
            '纪录片':1,'短片':23,'情色':6,'同性':26,'音乐':14,'歌舞':7,'家庭':28,'儿童':8,'传记':2,'历史':4,
            '战争': 22,'犯罪':3,'西部': 27,'奇幻':16,'冒险':15,'灾难':12,'武侠':29,'古装':30,'运动':18,'黑色电影':31,}

url='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

def findkey(Value):
    for key in movie_type.keys():
        if Value==movie_type[key]:
            return key

movies={}

def _Crawler_():
    for type in movie_type.values():
        precent=100
        tag=findkey(type)
        content=[]
        while precent>=10:
            url='https://movie.douban.com/j/chart/top_list?type='+str(type)+'&interval_id='+str(precent)+'%3A'+str(precent-10)+'&action=&start=0&limit=10000'
            print(url)
            request=urllib.request.Request(url)
            response=urllib.request.urlopen(request)
            result=json.loads(response.read().decode())
            precent=precent-10
            content=content+result
            flash(url)
    
        dict={tag : content}
        movies.update(dict)




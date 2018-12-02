# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:06:54 2018

@author: 郑宗
"""

from flask import Flask,g,render_template,request,url_for,jsonify,flash,redirect,Response
from flask_cors import CORS
from db import RedisClient
from Getter import  getCountry,find

import datetime
import os

__all__ = ['app']
app = Flask(__name__)
app.secret_key = 'some_secret'
CORS(app)  #注意这里的CORS
current_time = datetime.datetime.now()

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/proxy')
def proxy():
    q = request.args.get('q')
    ip = q[0:find(q,':')]
    data =  getCountry(ip)
    return jsonify(data)

@app.route('/proxrpool_list_')
def proxrpool_list_():
    q = request.args.get('q')
    ip = q[0:find(q,':')]
    data =  getCountry(ip)
    flash_data = '''
        &nbsp; ip  : %s  <br>
        &nbsp; 地区: %s   <br>
        &nbsp; 国家: %s   <br>
        &nbsp; 经纬度: %f ,%f   <br> 
        &nbsp; 类型  : %s       <br>
    ''' %(data['ip'],data['continent_name'],data['country_name'],data['latitude'],data['longitude'],data['type'])
    flash(flash_data,'success')
    return redirect(url_for('proxypool_list'))

@app.route('/random')
def get_proxy():
    """
    获取随机可用代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/all')
def get_all():
    """
    获取全部可用代理
    :return: 所有代理
    """
    conn = get_conn()
    return "{}".format(conn.list())

@app.route('/count')
def get_counts():
    """
    获取代理池总量
    :return:代理吃总量
    """
    conn = get_conn()
    return str(conn.count())

@app.route('/')
def Index():
    return render_template(
        'starter.html')
    
    
@app.route('/proxypool_instruction')
def proxypool_instruction():
    return render_template(
        'proxypool_instruction.html')

@app.route('/proxypool_list', methods=['POST','GET'])    
def proxypool_list():
    redis = RedisClient()
    proxy_list = redis.list()
    proxy_list = sorted(proxy_list, key=lambda x : x[1],reverse=True)

    IP = [proxy_list[i][0] for i in range(0,len(proxy_list))]
    PORT = [proxy_list[i][1] for i in range(0,len(proxy_list))]
    IP_PORT = dict(zip(IP, PORT))
    
    if request.method == 'POST':
        resolve_proxy= request.get_json()['ip']
        print(resolve_proxy)
        render_template(
        'proxypool_list.html',IP_PORT=enumerate(IP_PORT.items()),current_time=current_time,resolve_proxy=resolve_proxy) 
    
    return render_template(
        'proxypool_list.html',IP_PORT=enumerate(IP_PORT.items()),current_time=current_time,resolve_proxy='None') 

    

@app.route('/proxypool_api')
def proxypool_api():
    return render_template(
        'proxypool_api.html')

@app.route('/proxypool_code')
def proxypool_code():
    return render_template(
        'proxypool_code.html')

    
@app.route("/post/list/<page>/")
def my_list(page):
    # return "my list"
    print(page)
    return url_for("my_list",page=page,count=2)


#############################################################
import eventlet
eventlet.monkey_patch()
from other_spider.Douban_movie import _Crawler_ 

@app.route('/douban')
def douban():
    return render_template(
        'douban.html')
def event():
    for i in range(0,5):
        print('data:%d \n\n' % i)
        yield 'data:%d \n\n' % i
        eventlet.sleep(1)


@app.route('/douban_stream/', methods=['GET', 'POST'])
def douban_stream():
    
    return Response(_Crawler_(), mimetype="text/event-stream") # 注意这里的响应类型


from flask import send_file, send_from_directory
@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    filename = request.args.get("filename")
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = os.getcwd()  # 假设在当前目录
    return send_from_directory(directory, filename, as_attachment=True)

############################################################################


if __name__ == '__main__':
    app.debug = True
    app.run()

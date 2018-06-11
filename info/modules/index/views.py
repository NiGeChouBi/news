#coding:utf8
import logging

from flask import current_app,render_template
from info import redis_store
from . import index_blu

@index_blu.route('/',methods=["GET","POST"])
def hello_world():


    return render_template('news/index.html')


#每个网站都会发送请求/favicon.ico,去加载logo图片
#如果指定访问static中的内容, current_app.send_static_file(),自动寻找static中的内容,返回响应体对象
@index_blu.route('/favicon.ico')
def web_log():

    return current_app.send_static_file('news/favicon.ico')
# python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 0001 10:53
# @Author  : liudinglong
# @Site    : 
# @File    : app.py
# @Software: PyCharm


from flask import Flask
import config


#初始化flask对象
app = Flask(__name__)  #初始化程序实例,为flask类创建一个app实例,并带参数name
app.config.from_object(config)
#装饰器
@app.route('/')   #创建路由和视图函数
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '这是动态路由,%s' % name

#当前文件作为入口程序运行，就执行app.run()
if __name__ == '__main__':
    app.run()

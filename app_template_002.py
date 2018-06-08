# python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 0004 15:59
# @Author  : liudinglong
# @Site    : 
# @File    : app_template_002.py
# @Software: PyCharm

from flask import Flask
from jinja2 import PackageLoader, Environment
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)



if __name__ == '__main__':
    app.run()
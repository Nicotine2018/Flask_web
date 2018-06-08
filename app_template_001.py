# python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 0001 16:41
# @Author  : liudinglong
# @Site    : 
# @File    : app_template_001.py
# @Software: PyCharm



from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html5.html')

@app.route('/user/name')
def user(name):
    return render_template('home.html',name=name)

if __name__ == '__main__':
    app.run()
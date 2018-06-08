# python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 0004 17:00
# @Author  : liudinglong
# @Site    : 
# @File    : app_template_003.py
# @Software: PyCharm

from  flask import Flask
from flask_bootstrap import Bootstrap

from flask import render_template

app = Flask(__name__)

bootstarp = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>this is flaskbootstraptest %s</h>'%name
# @app.route('/service')
# def service():
#     return 'service'
#
# @app.route('/about')
# def about():
#     return 'about'



if __name__ == '__main__':
    app.run(debug=True)
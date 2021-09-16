#!/usr/bin/env python
# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)
app.run(debug=True)

# レンダリングテンプレート
@app.route('/')
def top():
    name = "top"
    return render_template('top.html', title='top page', name=name)

# app内でのURI設定
@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'

@app.route('/healthCheck')
def healthCheck():
    return 'OK'

# ブループリントの読み込み
import subapp as sub
app.register_blueprint(sub.app)

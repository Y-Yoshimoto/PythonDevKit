#!/usr/bin/env python
# coding:utf-8
from flask import Flask, request, jsonify
app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

@app.route('/healthCheck')
def hello_world():
    return 'OK'

## データ登録 ################################
import accessormongo
app.register_blueprint(accessormongo.app, url_prefix='/data')

## データ取得 ################################
#import getdata as getdata
#app.register_blueprint(getdata.app)

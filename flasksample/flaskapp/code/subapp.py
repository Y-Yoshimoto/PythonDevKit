#!/usr/bin/env python
# coding:utf-8
# Flaskのインポート，Blueprintのインポート
from flask import Blueprint, request, jsonify
import json

#Blueprintでモジュールの登録
app = Blueprint('sub', __name__)

@app.route('/subg/<word>', methods=['GET'])
def sub_get(word):
    return word

@app.route('/sub/<word>', methods=['POST'])
def sub_post(word):
    body = json.loads(request.get_data().decode().strip())
    return body
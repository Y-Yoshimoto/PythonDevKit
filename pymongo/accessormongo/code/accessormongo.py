#!/usr/bin/env python
# coding:utf-8
# Flaskのインポート，Blueprintのインポート
from flask import Blueprint, request, jsonify, abort
import json
# Loggerの設定
from logging import getLogger
logger = getLogger(__name__)


#Blueprintでモジュールの登録
app = Blueprint('accessormongo', __name__)

# MongoDB接続
import MongoConnector.Connector as MongoC
MC = MongoC.Connector("Sampledb")

### データ取得 #################################
@app.route('/<Collection>/', methods=['GET'])
def all_get(Collection):
    """コレクション内の全データを取得"""
    data = MC.getAllData(Collection)
    if len(data) == 0:
        abort(404)
    return jsonify(data)

@app.route('/<Collection>/max', methods=['GET'])
def getMax(Collection):
    """コレクション内の指定カラムの最大値を取得"""
    column = request.args.get("column", type=str)
    if column is None:
        abort(400)
    max = MC.searchMaxValue(Collection,column)
    if max == "Nodata":
        abort(404)
    return jsonify(max)

### データ登録 #################################
@app.route('/<Collection>/one', methods=['POST'])
def insertData(Collection):
    """コレクションに1レコードを追加"""
    body = request.get_data().decode().strip()
    response = {"insertRecords": MC.insertData(Collection, json.loads(body))}
    return jsonify(response)

@app.route('/<Collection>/', methods=['POST'])
def insertManydata(Collection):
    """コレクションにレコードを追加"""
    body = request.get_data().decode().strip()
    response = {"insertRecords": MC.insertBulkdata(Collection, json.loads(body))}
    return jsonify(response)

### インデックス追加 ###########################
@app.route('/<Collection>/addIndex', methods=['GET'])
def addIndex(Collection):
    """コレクションの指定カラムにインデックスを追加"""
    column = request.args.get("column", type=str)
    response = MC.addIndex(Collection,column)
    return jsonify(column)


### データ更新 #################################
@app.route('/<Collection>/', methods=['PATCH'])
def updateValueMany(Collection):
    """コレクションの指定カラムが指定した値のデータを削除"""
    body = request.get_data().decode().strip()
    filter=json.loads(body)["filter"]
    update=json.loads(body)["update"]
    response = MC.updateValueMany(Collection,filter, update)
    return jsonify(response)
#!/usr/bin/env python
# coding:utf-8
import datetime


# 関数定義
def echoArg(word):
    """引数で受け取った値を表示"""
    print("Argument is " + word)


def date():
    """現在時刻を指定のフォーマットで表示"""
    print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))


def add(a, b):
    """2つの引数を足し算して結果を返す"""
    return a + b


def product(a, b):
    """2つの引数を掛け算して結果を返す"""
    return a * b

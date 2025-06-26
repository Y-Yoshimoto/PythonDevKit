#!/usr/bin/env python
# coding: utf-8
"""
ユーザー管理システムのテスト実行スクリプト
"""

import sys
import os

# パスを追加してユーザーモジュールをインポートできるようにする
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from user.example import example_usage

if __name__ == "__main__":
    example_usage()

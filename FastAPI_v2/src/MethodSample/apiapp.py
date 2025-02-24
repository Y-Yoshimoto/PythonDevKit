#!/usr/bin/env python
# coding:utf-8
# モデル読み込み
from .model import SampleData
from fastapi import APIRouter

# ログ設定
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(filename)s:%(lineno)d %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# APIルータ
router = APIRouter()


@router.get("/sample/", include_in_schema=False)
def read_root():
    # Rootパス用
    return {"Path": "sample/root"}


@router.get("/methodsample/{id}")
def sample_get(id: int):
    """
    Getメソッドのサンプル

    Args:
        id (int): アイテムのID

    Returns:
        data (SampleData): IDと情報を含む辞書
    """
    returnData = SampleData(**{'id': id})
    print(returnData)
    return returnData

    # return returnData


@router.post("/methodsample/")
def sample_post(data: SampleData):
    """
    Postメソッドのサンプル
    bodyで受け取ったnameで、デフォルト値を上書きして返す

    Args:
        data (SampleData): 更新データ

    Returns:
        dict: IDと情報を含む辞書

    """
    return data

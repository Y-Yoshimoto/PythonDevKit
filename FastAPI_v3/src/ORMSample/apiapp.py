#!/usr/bin/env python
# coding:utf-8
from fastapi import APIRouter
router = APIRouter()


@router.get("/sample/")
def read_root():
    # Rootパス用
    return {"Path": "sample/root"}


@router.get("/sample/{id}")
def read_item(id: int, q: str = None):
    """
    idとオプションのクエリパラメータqを受け取り、それらを含む辞書を返すエンドポイント。

    Args:
        id (int): アイテムのID。
        q (str, optional): オプションのクエリパラメータ。デフォルトはNone。

    Returns:
        dict: IDとクエリパラメータqを含む辞書。
    """
    return {"id": id, "q": q}

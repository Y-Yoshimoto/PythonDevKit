#!/usr/bin/env python
# coding:utf-8
from fastapi import APIRouter
router = APIRouter()


# Rootパス用
@router.get("/sub/")
def read_root():
    return {"Path": "sub/root"}

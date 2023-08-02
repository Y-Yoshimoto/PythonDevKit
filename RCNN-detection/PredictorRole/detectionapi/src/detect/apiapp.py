#!/usr/bin/env python
# coding:utf-8
from fastapi import APIRouter

router = APIRouter()

# Rootパス用
@router.get("/detect/")
def read_root():
    return {"Path": "detect/root"}

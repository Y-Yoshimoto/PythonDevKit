from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
# 参考ドキュメント
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-models

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=False)
    authority: str = Field(index=True)
    name: str = Field(index=False)
    age: int | None = Field(default=None, index=False)
    secret_name: str
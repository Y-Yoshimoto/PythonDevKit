from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

# 参考: https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql
dbuser = 'user'
dbpassword = 'password'
dbhost = 'localhost'
dbport = '5432'
dbname = 'dbname'
postgresql_url = f"postgresql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}"
engine = create_engine(postgresql_url, echo=True)

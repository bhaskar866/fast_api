from typing import Union

from fastapi import FastAPI

from models import Test_db


from config.db import conn

app = FastAPI()

Res = list(conn.learn_server_side.Test_db.find())


@app.get("/{var}")
def fast_api(var:str):
    return Res[var]
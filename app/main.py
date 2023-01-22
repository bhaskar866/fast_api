from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def fast_api():
    return "Hello Bhaskar"


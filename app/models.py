from pydantic import BaseModel

class Test_db(BaseModel):
    name: str
    email: str
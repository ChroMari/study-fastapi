from pydantic import BaseModel

class User_info(BaseModel):
    name: str
    age: int

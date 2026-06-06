from pydantic import BaseModel

class User(BaseModel):
    Name:str
    Age:int
    Salary:float
    
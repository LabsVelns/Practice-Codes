from fastapi import FastAPI
import uvicorn as uv
from Pydantic_classes import User

app = FastAPI(title="FastAPI-with-Swagger/Openapi")

@app.get('/')
def index():
    return "Hello-People-this-is-the-beginning"

@app.get('/Welcome')
def get_name(name : str):
    return {f"Hi {name} it is very nice to meet you."}

@app.post('/Welcome/Details')
def get_details(Details:User):
    Details = Details.model_dump()
    Name = Details["Name"]
    Age = Details["Age"]
    Salary = Details["Salary"]

    return {f"Hi {Name} it is very nice to meet you. Your age is {Age} and your salary is {Salary}"}



if __name__ == '__main__':
    uv.run(app,host = "127.0.0.1",port = 8000)
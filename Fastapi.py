from fastapi import FastAPI
import uvicorn as uv

app = FastAPI(title="FastAPI-with-Swagger/Openapi")

@app.get('/')
def index():
    return "Hello-People-this-is-the-beginning"

@app.get('/Welcome')
def get_name(name : str):
    return {f"Hi {name} it is very nice to meet you."}


if __name__ == '__main__':
    uv.run(app,host = "127.0.0.1",port = 8000)
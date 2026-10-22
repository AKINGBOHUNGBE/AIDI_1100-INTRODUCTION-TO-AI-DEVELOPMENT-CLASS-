# importing fastAPI and other modules
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/add/{a}/{b}")
#creating a sum function
def add(a:int,b:int):
    """
    this is a function that takes two integers as input and returns their sum

    """
    return {"sum":int(a)+int(b)} # making sure that the input is integer

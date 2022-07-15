from fastapi import FastAPI
from Cyphers.cesar import Cesar

app = FastAPI()

#Routes

@app.get("/")
def index(value = None):
    if value == None:
        return {
        "Return" : "Hello World!"
    }
    else:
        return {
        "Message" : value,
        "Return" : "Hello World!"
    }

@app.get("/cesar")
def cypherCesar(text : str, key : int = 3):
    return {
        "Main Text": text,
        "Encrypy Text" : Cesar(text, key)
    }
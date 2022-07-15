from fastapi import FastAPI
from Cyphers.cesar import cesar

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
def cypherCesar(text : str):
    return {
        "Main Text": text,
        "Encrypy Text" : cesar(text)
    }
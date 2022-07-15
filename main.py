from fastapi import FastAPI
from Cyphers.cesar import Cesar
from Cyphers.morse import Morse

app = FastAPI()

#Routes

@app.get("/cesar")
def cypherCesar(text : str, key : int = 3):
    return {
        "Main Text": text,
        "Encrypt Text" : Cesar(text, key)
    }

@app.get("/morse")
def morseCode(text : str):
    return {
        "Main Text": text,
        "Encrypt Text" : Morse(text)
    }
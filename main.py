from fastapi import FastAPI
app = FastAPI()

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
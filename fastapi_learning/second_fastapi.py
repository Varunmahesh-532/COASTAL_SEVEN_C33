from fastapi import FastAPI

app = FastAPI()
@app.get('/students')
def student():
    return {
        "name": "Varun",
        "role": "Bankend Developer"
    }


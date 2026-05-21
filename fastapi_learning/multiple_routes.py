from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return{
        "message": "welcome to FastAPI"
    }

#About route
@app.get("/about")
def about():
    return {
        "This is About Page"
    }

#Student Route
@app.get("/students")
def students():
    return {
        "student": [
            "varun",
            "Mahesh", 
            "Kumar"
        ]
    }

#Contact Route
@app.get('/contact')
def contact():
    return {
        "email" : "varun@gmail.com"
    }


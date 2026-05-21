from fastapi import FastAPI

app = FastAPI()

student_data = {
    1: {
        "name": "varun",
        "age": 21
    },
    2: {
        "name": "mahesh",
        "age": 22
    },
    3:{
        "name": "kiran",
        "age": 23
    }
}

@app.get('/')
def home():
    return{
        "Student API"
    }

@app.get("/student/{student_id}")
def get_student(student_id: int):
    student = student_data.get(student_id)
    if student:
        return student
    return {
        "error": "Student not found"
    }

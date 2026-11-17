
from fastapi import FastAPI

app = FastAPI()

# GET API - Get student details
@app.get("/student")
def get_student():
    return {
        "name": "Abhishek",
        "age": 22,
        "course": "Backend Development"
    }


# POST API - Add a new student
@app.post("/student")
def add_student(name: str, age: int):
    return {
        "message": "Student added successfully!",
        "name": name,
        "age": age
    }
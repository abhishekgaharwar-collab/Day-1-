from fastapi import FastAPI

app = FastAPI()

# Temporary student data
student = {
    "name": "Abhishek",
    "age": 22,
    "course": "Backend Development"
}


# 1. GET API - Get student details
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI Backend!"}


@app.get("/student")
def get_student():
    return student


# 2. POST API - Add a new student
@app.post("/student")
def add_student(name: str, age: int):
    student["name"] = name
    student["age"] = age
    return {
        "message": "Student added successfully",
        "student": student
    }


# 3. PUT API - Update student details
@app.put("/student")
def update_student(name: str, age: int):
    student["name"] = name
    student["age"] = age
    return {
        "message": "Student updated successfully",
        "student": student
    }


# 4. DELETE API - Delete student details
@app.delete("/student")
def delete_student():
    student.clear()
    return {"message": "Student deleted successfully"}
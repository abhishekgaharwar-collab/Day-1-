# FastAPI - Simple GET and POST API

## About the Project
This is my first FastAPI project. I created two simple APIs using Python and FastAPI.

The project demonstrates how to get student details and add new student information using GET and POST methods.

## Technologies Used
- Python
- FastAPI
- Uvicorn

## Project Structure

```text
Day 1 – Backend Plan/
│
├── main.py
├── README.md
└── venv/
```

## Installation and Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install FastAPI

```bash
pip install "fastapi[standard]"
```

### 4. Run the Project

```bash
fastapi dev main.py
```

Server will start at:

http://127.0.0.1:8000

## API Endpoints

### 1. GET API - Get Student Details

**Endpoint:**
```http
GET /student
```

**URL:**
http://127.0.0.1:8000/student

**Description:**

Returns student information such as name, age, and course.

**Response:**

```json
{
    "name": "Abhishek",
    "age": 22,
    "course": "Backend Development"
}
```

### 2. POST API - Add New Student

**Endpoint:**
```http
POST /student
```

**Description:**

Accepts student name and age and returns a success message with the submitted details.

**Parameters:**

- name: Student name (string)
- age: Student age (integer)

**Example:**

```text
/student?name=Rahul&age=23
```

**Response:**

```json
{
    "message": "Student added successfully!",
    "name": "Rahul",
    "age": 23
}
```

## API Documentation

FastAPI provides automatic interactive API documentation.

Open this URL in your browser:

http://127.0.0.1:8000/docs

You can test both GET and POST APIs using Swagger UI.

## What I Learned

- Introduction to FastAPI.
- Creating a FastAPI application.
- Understanding GET and POST methods.
- Creating API endpoints.
- Returning JSON responses.
- Testing APIs using Swagger UI.

## Author

Abhishek Gaharwar

**Learning Backend Development with Python and FastAPI.**

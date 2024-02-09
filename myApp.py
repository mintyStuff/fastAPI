from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
   1 : {
            "id": 1,
            "name": "Jan"
        },
   2 : {
            "id": 2,
            "name": "Bravo"
        },
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/users")
def getUsers():
    return users.values()

@app.get("/users/{id}")
def getUser(id: int = Path(description = "Id of user")):
    return users[id]

@app.get("/items")
def getItem(name: Optional[str] = None):
    print(name)

@app.post("/student")
def createStudent(student: Student):
    print(student)
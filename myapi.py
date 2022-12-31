from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
students={
    1:{
        "name": "ojiambo",
        "age":17,
        "class":"Year 1"
    } ,2 :{
        "name": "felix",
        "age":18,
        "class":"Year 2"
    }
}
class Student(BaseModel):
    name:str
    age:int
    year:str
    
#END POINT METHODS(get, post,put,delete)
@app.get("/")
def index():
    return {"name":"first data entry"}
@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(None,description="The ID of the student you wanna view",gt=0)):
    return students[student_id]
@app.get("/get-by-name/student_id")
def get_student(*,student_id:int,name:Optional[str]=None,test:int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"} 
   #Request Body and Post Method
@app.post("/create-student/{student_id")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    students[student_id]=student
    return students[student_id]   
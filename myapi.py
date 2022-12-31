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
class  UpdateStudent(BaseModel):
    name:Optional[str] =None    
    age:Optional[int]=None
    year:Optional[str]=None
        
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
#Put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name !=None:
         students[student_id].name=student.name
    if student.age !=None:
         students[student_id].age=student.age
    if student.year !=None:
         students[student_id].year=student.year
                   
    return students[student_id]
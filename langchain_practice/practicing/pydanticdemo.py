from pydantic import BaseModel
from typing import Optional

class Student (BaseModel):
    name : str = "default"     #if name is not mention u can set default value as well
    age : Optional[int] = None


new_student = {
    "name" : "haroon",
    "age" : "32" # it will convert this into int (type conversion)
}


# new_student = {    --> this will throw error
#     "name" : 23
# }

student = Student(**new_student)

print(student.age)
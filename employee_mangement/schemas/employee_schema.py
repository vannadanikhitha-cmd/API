from pydantic import BaseModel
from pydantic import EmailStr
from datetime import date
class EmployeeCreate(BaseModel):

    first_name: str
    last_name: str
    email: str
    phone: str
    gender: str
    age: int
    designation: str
    joining_date: date
    salary: float
    department_id: int


class EmployeeUpdate(BaseModel):

    designation: str
    salary: float


class EmployeeResponse(BaseModel):

    employee_id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True
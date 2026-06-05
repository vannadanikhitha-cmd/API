from pydantic import BaseModel, field_validator
from pydantic import EmailStr
from datetime import date
from employee_mangement.validators.employee_validator import validate_age
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
    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Employee age must be at least 18")
        return value

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
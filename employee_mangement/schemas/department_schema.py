from pydantic import BaseModel

class DepartmentCreate(BaseModel):

    department_name: str

class DepartmentResponse(BaseModel):

    id: int

    department_name: str

    class Config:
        from_attributes = True
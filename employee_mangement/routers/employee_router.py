from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from employee_mangement.database.session import get_db

from employee_mangement.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeResponse
)

from employee_mangement.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    delete_employee
)
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# Create Employee
@router.post("/create")
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee(db, employee)

# Get All Employees
@router.get("/fetch_employees")
def fetch_all_employees(
    db: Session = Depends(get_db)
):
    return get_all_employees(db)

# Get Employee By ID
@router.get("/view/{employee_id}")
def fetch_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

# Delete Employee
@router.delete("/delete/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_employee(db, employee_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }
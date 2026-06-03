from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.session import get_db

from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeResponse
)

from services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/")
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return create_employee(
        db,
        employee
    )


@router.get("/")
def fetch_all_employees(
    db: Session = Depends(get_db)
):

    return get_all_employees(db)


@router.get("/{employee_id}")
def fetch_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = get_employee_by_id(
        db,
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.delete("/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_employee(
        db,
        employee_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message":
        "Employee deleted successfully"
    }
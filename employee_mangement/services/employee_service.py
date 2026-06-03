from models.employee_model import Employee

def create_employee(
    db,
    employee
):

    emp = Employee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        phone=employee.phone,
        gender=employee.gender,
        age=employee.age,
        designation=employee.designation,
        joining_date=employee.joining_date,
        salary=employee.salary,
        department_id=employee.department_id
    )

    db.add(emp)

    db.commit()

    db.refresh(emp)

    return emp


def get_all_employees(db):

    return db.query(Employee).all()


def get_employee_by_id(
    db,
    employee_id
):

    return (
        db.query(Employee)
        .filter(
            Employee.employee_id == employee_id
        )
        .first()
    )


def delete_employee(
    db,
    employee_id
):

    employee = (
        db.query(Employee)
        .filter(
            Employee.employee_id == employee_id
        )
        .first()
    )

    if employee:

        db.delete(employee)

        db.commit()

        return True

    return False
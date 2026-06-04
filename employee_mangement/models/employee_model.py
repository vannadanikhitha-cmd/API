from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date

from employee_mangement.models.base import Base

class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True
    )

    phone = Column(
        String(20)
    )

    gender = Column(
        String(20)
    )

    age = Column(
        Integer
    )

    designation = Column(
        String(100)
    )

    joining_date = Column(
        Date
    )

    salary = Column(
        Float
    )

    department_id = Column(
        Integer
    )
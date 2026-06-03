from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey

from models.base import Base

class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(50),
        nullable=False
    )

    last_name = Column(
        String(50)
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(15)
    )

    gender = Column(
        String(10)
    )

    age = Column(Integer)

    designation = Column(
        String(100)
    )

    joining_date = Column(Date)

    salary = Column(
        Numeric(10,2)
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )
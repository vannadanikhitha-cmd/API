from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from employee_mangement.models.employee_model import Base

class Department(Base):

    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True
    )

    department_name = Column(
        String(100),
        unique=True
    )
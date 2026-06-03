from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from models.base import Base

class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False
    )
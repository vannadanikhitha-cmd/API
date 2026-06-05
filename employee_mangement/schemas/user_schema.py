from pydantic import BaseModel, field_validator
import re

class UserRegister(BaseModel):
    username: str
    password: str
    role: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):

        if len(value) < 4:
            raise ValueError(
                "Username must contain at least 4 characters"
            )

        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )

        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "Password must contain one uppercase letter"
            )

        if not re.search(r"[a-z]", value):
            raise ValueError(
                "Password must contain one lowercase letter"
            )

        if not re.search(r"\d", value):
            raise ValueError(
                "Password must contain one number"
            )

        return value

    @field_validator("role")
    @classmethod
    def validate_role(cls, value):

        allowed_roles = [
            "admin",
            "manager",
            "employee"
        ]

        if value.lower() not in allowed_roles:
            raise ValueError(
                "Role must be admin, manager or employee"
            )

        return value
class UserLogin(BaseModel):
    username: str
    password: str
from pydantic import BaseModel

class Settings(BaseModel):

    DB_SERVER: str = ".\\SQLEXPRESS"
    DB_NAME: str = "employee_management"

    SECRET_KEY: str = "employee_management_secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
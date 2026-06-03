from fastapi import FastAPI

from routers.auth_router import router as auth_router
from routers.employee_router import router as employee_router

from database.connection import engine
from models.base import Base

app = FastAPI(
    title="Employee Management System",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(employee_router)

@app.get("/")
def home():

    return {
        "message": "Employee Management System"
    }

@app.get("/health")
def health():

    return {
        "status": "running"
    }
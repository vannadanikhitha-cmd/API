from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from employee_mangement.database.connection import engine
from employee_mangement.models.employee_model import Base

from employee_mangement.routers.auth_router import router as auth_router
from employee_mangement.routers.employee_router import router as employee_router
from employee_mangement.routers.page_router import router as page_router
from employee_mangement.models.employee_model import Employee
from employee_mangement.models.user_model import User
from employee_mangement.models.base import Base
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Employee Management System"
)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

app.mount(
    "/static",
    StaticFiles(
        directory=os.path.join(
            BASE_DIR,
            "static"
        )
    ),
    name="static"
)

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(page_router)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {
        "status": "running"
    }
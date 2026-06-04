from fastapi import FastAPI
import os
from fastapi.staticfiles import StaticFiles


from database.connection import engine

from models.employee_model import Base

from routers.auth_router import router as auth_router
from routers.employee_router import router as employee_router
from routers.page_router import router as page_router

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

@app.get("/")
def home():

    return {
        "message":
        "Employee Management System"
    }


@app.get("/health")
def health():

    return {
        "status":
        "running"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
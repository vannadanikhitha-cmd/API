from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

templates = Jinja2Templates(
    directory=os.path.join(
        BASE_DIR,
        "templates"
    )
)
@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request}
    )


@router.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )

@router.get("/employees-page")
async def employees(request: Request):
    return templates.TemplateResponse(
        "employees.html",
        {
            "request": request
        }
    )

@router.get("/add-employee")
async def add_employee(request: Request):
    return templates.TemplateResponse(
        "add_employee.html",
        {
            "request": request
        }
    )
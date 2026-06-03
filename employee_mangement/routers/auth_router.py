from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.session import get_db

from schemas.user_schema import (
    UserRegister,
    UserLogin
)

from services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    result = register_user(
        db,
        user.username,
        user.password,
        user.role
    )

    if not result:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return {
        "message": "User Registered Successfully"
    }


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        user.username,
        user.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
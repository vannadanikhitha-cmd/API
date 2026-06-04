from sqlalchemy.orm import Session

from employee_mangement.models.user_model import User

from employee_mangement.utils.password_handler import (
    hash_password,
    verify_password
)

from employee_mangement.utils.jwt_handler import (
    create_access_token
)

def register_user(
    db: Session,
    username: str,
    password: str,
    role: str
):

    existing_user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )

    if existing_user:

        return None

    user = User(
        username=username,
        password=hash_password(password),
        role=role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(
    db: Session,
    username: str,
    password: str
):

    user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )

    if not user:

        return None

    if not verify_password(
        password,
        user.password
    ):

        return None

    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role
        }
    )

    return token
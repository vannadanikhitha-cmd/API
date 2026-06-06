from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Header
from jose import jwt

from jwt_auth_config import SECRET_KEY
from jwt_auth_config import ALGORITHM

app = FastAPI(title="JWT Authentication")

USERS = {
    "admin": "admin123"
}


@app.post("/login")
def login(username: str, password: str):

    if username not in USERS:
        raise HTTPException(
            status_code=401,
            detail="User Not Found"
        )

    if USERS[username] != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = jwt.encode(
        {
            "username": username
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token
    }


@app.get("/employees")
def employees(
    authorization: str = Header(None)
):

    try:

        token = authorization.split(" ")[1]

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "message": "Success",
            "user": payload["username"]
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
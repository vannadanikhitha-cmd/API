from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException

from oauth2_auth_config import SECRET_TOKEN

app = FastAPI(title="OAuth2 Authentication")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


@app.post("/login")
def login():

    return {
        "access_token": SECRET_TOKEN,
        "token_type": "bearer"
    }


@app.get("/employees")
def employees(
    token: str = Depends(oauth2_scheme)
):

    if token != SECRET_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return {
        "message": "OAuth2 Authentication Success"
    }
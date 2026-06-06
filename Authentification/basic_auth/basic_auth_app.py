from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException
from connection import engine
app = FastAPI()

security = HTTPBasic()
@app.get("/profile")
def profile(
    credentials: HTTPBasicCredentials = Depends(security)
):

    if credentials.username:
        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    return {
        "message": "Login Successful"
    }
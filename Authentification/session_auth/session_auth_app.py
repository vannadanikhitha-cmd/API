from fastapi import FastAPI
from fastapi import Cookie
from fastapi.responses import JSONResponse

from session_auth_config import SESSION_ID

app = FastAPI(title="Session Authentication")


@app.post("/login")
def login():

    response = JSONResponse(
        content={
            "message": "Login Successful"
        }
    )

    response.set_cookie(
        key="session_id",
        value=SESSION_ID
    )

    return response


@app.get("/profile")
def profile(
    session_id: str = Cookie(None)
):

    if session_id != SESSION_ID:
        return {
            "message": "Unauthorized"
        }

    return {
        "message": "Authorized User"
    }
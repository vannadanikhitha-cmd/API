from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import hashlib

app = FastAPI()

USERNAME = "nikki"
PASSWORD = "nikki@123"

REALM = "employee_management"
NONCE = "123456"

@app.get("/profile")
def profile(request: Request):

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return JSONResponse(
            status_code=401,
            content={"detail": "Authentication Required"},
            headers={
                "WWW-Authenticate":
                f'Digest realm="{REALM}", nonce="{NONCE}", algorithm=MD5'
            }
        )

    return {
        "message": "Digest Authentication Success"
    }
from fastapi import FastAPI, Header, HTTPException
from bearer_toekn_config import TOKEN

app = FastAPI(title="Bearer Token Authentication")

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"}
]

@app.get("/")
def home():
    return {
        "message": "Bearer Token Authentication"
    }

@app.get("/employees")
def get_employees(
    authorization: str = Header(None)
):

    if authorization != f"Bearer {TOKEN}":
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return employees
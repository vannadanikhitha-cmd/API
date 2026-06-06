from fastapi import FastAPI, Header, HTTPException
from api_auth_config import API_KEY

app = FastAPI()

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"}
]

@app.get("/employees")
def get_employees(x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return employees
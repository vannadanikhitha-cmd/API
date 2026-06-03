from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_connection import get_connection

app = FastAPI()

class EmployeeRequest(BaseModel):
    name: str

@app.post("/getage")
def get_age(employee: EmployeeRequest):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT age FROM emp WHERE name = ?",
        (employee.name,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "age": row[0]
        }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
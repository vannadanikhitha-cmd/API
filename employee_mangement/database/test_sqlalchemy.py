# test_sqlalchemy.py

from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

params = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Nikhitha\\SQLEXPRESS;"
    "DATABASE=employee_management;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT @@VERSION"))
    print(result.fetchone())

print("SQLAlchemy Connected Successfully")
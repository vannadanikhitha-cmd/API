from sqlalchemy import create_engine
from urllib.parse import quote_plus

params = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SIVA\\SQLEXPRESS;"
    "DATABASE=employee_management;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
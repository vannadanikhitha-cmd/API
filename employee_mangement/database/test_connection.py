import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=employee_management;"
    "Trusted_Connection=yes;"
)

print("Connected Successfully")
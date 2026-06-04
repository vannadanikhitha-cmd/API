# database/debug_server.py

import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=employee_management;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT @@SERVERNAME")

print(cursor.fetchone()[0])

conn.close()
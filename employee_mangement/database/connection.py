from sqlalchemy import create_engine
from config.settings import settings

DATABASE_URL = (
    f"mssql+pyodbc://@{settings.DB_SERVER}/"
    f"{settings.DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)
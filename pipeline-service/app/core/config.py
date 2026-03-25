import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:root@localhost:5432/customer_db"
)

FLASK_BASE_URL = os.getenv(
    "FLASK_BASE_URL",
    "http://mock-server:5000"
)
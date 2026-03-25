import os
import logging

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:root@localhost:5432/customer_db"
)

FLASK_BASE_URL = os.getenv(
    "FLASK_BASE_URL",
    "http://mock-server:5000"
)

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
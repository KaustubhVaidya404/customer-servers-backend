import json
from config import DATA_FILE


def load_customers():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def get_all_customers():
    return load_customers()


def get_customer_by_id(customer_id):
    customers = load_customers()
    return next(
        (c for c in customers if c["customer_id"] == customer_id),
        None
    )
import requests
from sqlalchemy.orm import Session
from app.db.models import Customer
from app.core.config import FLASK_BASE_URL


def fetch_all_customers():
    page = 1
    limit = 10
    all_data = []

    while True:
        url = f"{FLASK_BASE_URL}/api/customers?page={page}&limit={limit}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch data from Flask")

        data = response.json()

        customers = data.get("data", [])
        if not customers:
            break

        all_data.extend(customers)

        # stop when last page
        if len(customers) < limit:
            break

        page += 1

    return all_data


def upsert_customers(db: Session, customers: list):
    processed = 0

    for c in customers:
        cid = str(c["customer_id"])
        
        existing = db.query(Customer).filter_by(
            customer_id=cid
        ).first()

        if existing:
            # UPDATE
            for key, value in c.items():
                if key == "customer_id":
                    value = str(value)
                setattr(existing, key, value)
        else:
            # INSERT
            c["customer_id"] = cid
            new_customer = Customer(**c)
            db.add(new_customer)


        processed += 1

    db.commit()
    return processed
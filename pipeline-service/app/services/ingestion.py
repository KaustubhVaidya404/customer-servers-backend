import requests
import logging
from sqlalchemy.orm import Session
from app.db.models import Customer
from app.core.config import FLASK_BASE_URL

logger = logging.getLogger(__name__)


def fetch_all_customers():
    page = 1
    limit = 10
    all_data = []

    logger.info("Starting to fetch all customers from mock-server")
    while True:
        url = f"{FLASK_BASE_URL}/api/customers?page={page}&limit={limit}"
        logger.debug(f"Fetching page {page} with limit {limit} from {url}")
        response = requests.get(url)

        if response.status_code != 200:
            logger.error(f"Failed to fetch data from Flask. Status: {response.status_code}, Response: {response.text}")
            raise Exception("Failed to fetch data from Flask")

        data = response.json()

        customers = data.get("data", [])
        logger.info(f"Fetched {len(customers)} customers from page {page}")
        if not customers:
            break

        all_data.extend(customers)

        # stop when last page
        if len(customers) < limit:
            break

        page += 1

    logger.info(f"Total customers fetched: {len(all_data)}")
    return all_data


def upsert_customers(db: Session, customers: list):
    logger.info(f"Starting upsert process for {len(customers)} customers")
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
    logger.info(f"Upsert process completed. Total records processed/upserted: {processed}")
    return processed
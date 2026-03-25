import json
import logging
from config import DATA_FILE

logger = logging.getLogger(__name__)


def load_customers():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            logger.debug(f"Loaded {len(data)} customers from {DATA_FILE}")
            return data
    except Exception as e:
        logger.error(f"Failed to load customers from {DATA_FILE}: {str(e)}")
        raise


def get_all_customers():
    return load_customers()


def get_customer_by_id(customer_id):
    customers = load_customers()
    return next(
        (c for c in customers if c["customer_id"] == customer_id),
        None
    )
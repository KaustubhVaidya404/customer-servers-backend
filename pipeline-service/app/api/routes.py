from fastapi import APIRouter, Depends, HTTPException
import logging
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Customer
from app.services.ingestion import fetch_all_customers, upsert_customers

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/api/ingest")
def ingest(db: Session = Depends(get_db)):
    logger.info("Received request for customer ingestion")
    try:
        customers = fetch_all_customers()
        count = upsert_customers(db, customers)
        logger.info(f"Ingestion successful. {count} records processed.")

        return {
            "status": "success",
            "records_processed": count
        }
    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    logger.info(f"Fetching customers: page={page}, limit={limit}")
    offset = (page - 1) * limit

    customers = db.query(Customer).offset(offset).limit(limit).all()
    total = db.query(Customer).count()
    logger.info(f"Found {len(customers)} customers (Total: {total})")

    return {
        "data": customers,
        "total": total,
        "page": page,
        "limit": limit
    }


@router.get("/api/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    logger.info(f"Fetching customer with ID: {customer_id}")
    customer = db.query(Customer).filter_by(customer_id=customer_id).first()

    if not customer:
        logger.warning(f"Customer with ID {customer_id} not found")
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer
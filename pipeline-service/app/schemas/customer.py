from pydantic import BaseModel
from datetime import date, datetime


class CustomerResponse(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone: str | None
    address: str | None
    date_of_birth: date | None
    account_balance: float | None
    created_at: datetime | None

    class Config:
        from_attributes = True
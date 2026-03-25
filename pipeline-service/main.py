from fastapi import FastAPI
import logging
from app.api.routes import router
from app.db.database import engine, Base
from app.core.config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Pipeline Service")
app.include_router(router)


@app.on_event("startup")
def startup_event():
    logger.info("Starting Pipeline Service...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



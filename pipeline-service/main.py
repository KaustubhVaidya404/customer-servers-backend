from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine, Base

app = FastAPI(title="Pipeline Service")
app.include_router(router)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



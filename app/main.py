from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routers import tasks


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo List API",
    description="REST API for managing todo tasks",
    version="1.0.0"
)


# Register routers
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Todo List API"
    }

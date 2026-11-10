from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routers import tasks


# Create database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Todo List API",
    description="REST API for managing todo tasks",
    version="1.0.0",
  lifespan=lifespan
)


# Register routers
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Todo List API"
    }

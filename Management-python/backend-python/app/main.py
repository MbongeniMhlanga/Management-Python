from fastapi import FastAPI
from app.routers import department, employee
from app.config import Base, engine

# Auto-create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(department.router)
app.include_router(employee.router)

@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"}

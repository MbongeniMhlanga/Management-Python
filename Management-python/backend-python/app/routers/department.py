from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.crud import crud
from app.config import SessionLocal
from typing import List

router = APIRouter(prefix="/departments", tags=["Departments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Department])
def read_departments(db: Session = Depends(get_db)):
    return crud.get_departments(db)

@router.get("/{id}", response_model=schemas.Department)
def read_department(id: int, db: Session = Depends(get_db)):
    db_dept = crud.get_department(db, id)
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_dept

@router.post("/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, department)

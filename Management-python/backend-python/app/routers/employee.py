from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.crud import crud
from app.config import SessionLocal
from typing import List

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@router.get("/", response_model=List[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@router.get("/{id}", response_model=schemas.Employee)
def read_employee_by_id(id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee_by_id(db, id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.get("/email/{email}", response_model=schemas.Employee)
def read_employee_by_email(email: str, db: Session = Depends(get_db)):
    emp = crud.get_employee_by_email(db, email)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{id}", response_model=schemas.Employee)
def update_employee(id: int, updates: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    emp = crud.update_employee(db, id, updates)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.delete("/{id}", response_model=schemas.Employee)
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

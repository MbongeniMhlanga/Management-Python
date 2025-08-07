from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

# --- DEPARTMENTS ---
def get_departments(db: Session):
    return db.query(models.Department).all()

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


# --- EMPLOYEES ---
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def update_employee(db: Session, employee_id: int, updates: schemas.EmployeeUpdate):
    db_emp = get_employee_by_id(db, employee_id)
    if not db_emp:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_emp, key, value)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def delete_employee(db: Session, employee_id: int):
    db_emp = get_employee_by_id(db, employee_id)
    if not db_emp:
        return None
    db.delete(db_emp)
    db.commit()
    return db_emp

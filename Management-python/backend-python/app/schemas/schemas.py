from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal



# ====================
# Department Schemas
# ====================

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    """Schema for creating a new department"""
    pass

class Department(DepartmentBase):
    """Schema for returning a department"""
    id: int

    model_config = {
        "from_attributes": True
    }


# ====================
# Employee Schemas
# ====================

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department_id: Optional[int]
    salary: Optional[Decimal]
    role: Optional[str]  # 👈 Add this line
    


class EmployeeCreate(EmployeeBase):
    """Schema for creating a new employee"""
    pass

class EmployeeUpdate(BaseModel):
    """Schema for updating an employee"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department_id: Optional[int] = None
    role: Optional[str] = None  # 👈 Also add it here if updates are allowed
    salary: Optional[Decimal]


class Employee(EmployeeBase):
    """Schema for returning an employee"""
    id: int

    model_config = {
        "from_attributes": True
    }

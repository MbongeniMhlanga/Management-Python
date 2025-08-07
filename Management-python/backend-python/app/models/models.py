from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.config import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=True)
    salary = Column(Numeric(10, 2), nullable=True)  # Use Numeric with precision

    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")

from database import Base
from sqlalchemy import Column, INTEGER, VARCHAR



class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(INTEGER, primary_key = True, index = True)
    employee_name =  Column(VARCHAR(1024))
    employee_email = Column(VARCHAR(1024), unique = True)
    password = Column(VARCHAR(1024))



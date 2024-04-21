from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Patient(BaseModel):
    id: None   
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str
    
class PatientUpdate(BaseModel):
    age: int = Field(default=None, nullable=True)
    weight: float
    height: float
    phone: str

class Doctor(BaseModel):
    id: None   
    name: str
    specialization: str
    phone: str
    is_available: bool = True
    
class DoctorUpdate(BaseModel):
    is_available: bool = True
    phone: int

class Appointment(BaseModel):
    id: None   
    patient_id: int
    doctor_id: int
    date: datetime
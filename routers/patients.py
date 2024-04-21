from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.models import Patient, PatientUpdate
from schemas.data import patients
import random

router = APIRouter()

@router.post("/patients/", status_code=status.HTTP_201_CREATED, response_model=Patient)
def create_patient(patient: Patient) -> Patient:
    patient.id = random.randint(1, 358721)  # Assign a random ID to the new patient
    patients.append(patient)
    return patient

@router.get("/patients/", response_model=List[Patient])
def get_all_patients() -> List[Patient]:
    return patients

@router.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int) -> Patient:
    for patient in patients:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

# @router.put("/patients/{patient_id}", response_model=Patient)
# def update_patient(patient_id: int, updated_patient: PatientUpdate) -> Patient:
#     for patient in patients:
#         if patient.id == patient_id:
#             patient.age = updated_patient.age
#             patient.weight = updated_patient.weight
#             patient.height = updated_patient.height
#             patient.phone = updated_patient.phone
#             return patient
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

@router.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_patient: PatientUpdate):
    for patient in patients:
        if patient.id == patient_id:
            patient.age = updated_patient.age
            patient.weight = updated_patient.weight
            patient.height = updated_patient.height
            patient.phone = updated_patient.phone
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@router.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            del patients[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
from fastapi import APIRouter, HTTPException
from typing import List
from schemas.models import Appointment
from schemas.data import appointments, doctors
import random

router = APIRouter()

@router.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: Appointment) -> Appointment:
    """Create a new appointment if a doctor is available."""
    appointment.id = random.randint(1, 358721)  # Assign a random ID to the appointment
    for doctor in doctors:
        if doctor.is_available:
            appointment.doctor_id = doctor.id
            appointments.append(appointment)
            doctor.is_available = False
            return appointment
    raise HTTPException(status_code=404, detail="No available doctors at the moment.")

@router.get("/appointments/", response_model=List[Appointment])
def get_all_appointments() -> List[Appointment]:
    return appointments

@router.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: int) -> dict:
    """Cancel an appointment and make the doctor available again."""
    for index, appointment in enumerate(appointments):
        if appointment.id == appointment_id:
            # Make the doctor available again
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
                    break
                del appointments[index]
            return {"status": "Appointment canceled"}
    raise HTTPException(status_code=404, detail="Appointment not found")


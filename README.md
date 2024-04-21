# Medical Appointment Application API

This FastAPI-based API facilitates appointment bookings between patients and doctors for a medical appointment application. It provides endpoints for managing patients, doctors, and appointments, allowing users to create, read, update, and delete records, as well as schedule and cancel appointments.

## Features

- CRUD endpoints for managing patients and doctors
- Appointment creation, cancellation, and completion functionality
- Doctor availability management

## Directory Structure

The project follows a modular structure for better organization and readability:

- **main.py**: Entry point for the FastAPI application. It includes routers for patients, doctors, and appointments.

- **models.py**: Defines Pydantic models (schemas) for the data entities in the application, including Patient, Doctor, and Appointment.

- **data.py**: Contains lists to store instances of patients, doctors, and appointments, serving as in-memory databases.

- **routers**: Directory containing router modules for handling HTTP requests related to different entities:

  - **patients.py**: Defines CRUD endpoints for patients.
  - **doctors.py**: Defines CRUD endpoints for doctors.
  - **appointments.py**: Defines endpoints for managing appointments.

- **schemas**: Directory containing Pydantic schemas for data validation and serialization:

  - **patient.py**: Defines Pydantic schemas for the Patient entity.
  - **doctor.py**: Defines Pydantic schemas for the Doctor entity.
  - **appointment.py**: Defines Pydantic schema for the Appointment entity.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/motunmarteen/Medical_App.git
2. Install the required dependencies:
   pip install -r requirements.txt
   
3. Run the FastAPI application:
   uvicorn main:app --reload

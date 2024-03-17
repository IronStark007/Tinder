from datetime import date, datetime
from typing import Dict, List
from uuid import UUID
from pydantic import BaseModel, root_validator

class CreateSchema(BaseModel):
    email: str
    password: str
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        pass1, pass2 = values.get('password'), values.get('confirm_password')
        if pass1 is not None and pass2 is not None and pass1 != pass2:
            raise ValueError('passwords do not match')
        return values

class LoginSchema(BaseModel):
    email: str
    password: str

class CoordinateSchema(BaseModel):
    long: float
    lat: float

class LocationSchema(BaseModel):
    state: str
    coordinate: Dict[CoordinateSchema,None]
    country: str
    city: str
 
class UserDataSchema(BaseModel):
   user_id: UUID
   name: str
   phone_number: int
   image: str
   desp: str
   location: Dict[LocationSchema, None]
   dob: date
   gender: str
   passion: List[str]
   job: str
   company : str
   created_at: datetime = datetime.utcnow()

class ResponseSchema(BaseModel):
    message: str
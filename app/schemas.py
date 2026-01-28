from pydantic import BaseModel
from datetime import date

class DOBRequest(BaseModel):
    dob: date

class AgeResponse(BaseModel):
    years: int
    months: int
    days: int

from fastapi import APIRouter, HTTPException
from app.services import calculate_age
from app.schemas import DOBRequest

router = APIRouter(prefix="/api", tags=["Age Calculator"])


@router.post("/calculate-age")
def get_age(data: DOBRequest):
    try:
        return calculate_age(data.dob)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

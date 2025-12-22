from fastapi import APIRouter
from app.services.hardware_service import get_hardware_info

router = APIRouter(
    prefix="",
    tags=["Hardware"]
)

@router.get("/hardware")
async def hardware_info():
    return get_hardware_info()

from fastapi import APIRouter
from app.services.system_service import get_system_info

router = APIRouter(prefix="/system", tags=["System"])


@router.get("")
def system_info():
    return get_system_info()

from fastapi import APIRouter
from app.services.monitoring_service import get_monitoring_info

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])


@router.get("")
def monitoring():
    return get_monitoring_info()

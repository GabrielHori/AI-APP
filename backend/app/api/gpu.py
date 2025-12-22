from fastapi import APIRouter
from app.services.gpu_service import get_gpu_info

router = APIRouter(
    tags=["GPU"]
)

@router.get("/gpu")
async def gpu_info():
    return get_gpu_info()

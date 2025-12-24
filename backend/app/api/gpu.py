from fastapi import APIRouter
from app.services.gpu_service import gpu_service

router = APIRouter()

@router.get("/info")
async def get_gpu_info():
    """
    Renvoie les infos GPU et VRAM en temps réel.
    """
    return gpu_service.get_gpu_stats()
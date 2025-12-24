from fastapi import APIRouter
from app.services.hardware_service import hardware_service

router = APIRouter()

# ON AJOUTE /hardware/ DEVANT usage pour correspondre au Frontend
@router.get("/hardware/usage")
async def get_hardware_usage():
    """
    Retourne l'utilisation CPU, RAM et Disque en temps réel.
    """
    stats = hardware_service.get_system_stats()
    return stats
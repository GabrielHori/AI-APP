from fastapi import APIRouter
from app.services.compatibility_service import check_models_compatibility

router = APIRouter(prefix="/models", tags=["Models"])


@router.get("/compatible")
def compatible_models():
    return check_models_compatibility()

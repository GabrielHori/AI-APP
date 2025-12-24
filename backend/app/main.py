from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Imports des routeurs
from app.api.hardware import router as hardware_router
from app.api.gpu import router as gpu_router
from app.api.system import router as system_router
from app.api.models import router as models_router
from app.api.monitoring import router as monitoring_router

# Initialisation de l'app
app = FastAPI(
    title="V1-IA-APP Backend",
    description="Backend local pour l'application IA",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enregistrement des routes
app.include_router(hardware_router, prefix="/api/v1", tags=["Hardware"])
app.include_router(gpu_router, prefix="/api/v1/gpu", tags=["GPU"])
app.include_router(system_router, prefix="/api/v1", tags=["System"])
app.include_router(models_router, prefix="/api/v1", tags=["Models"])
app.include_router(monitoring_router, prefix="/api/v1", tags=["Monitoring"])

@app.get("/")
def root():
    return {
        "message": "V1-IA-APP Backend is running", 
        "docs": "/docs",
        "version": "1.0.0"
    }
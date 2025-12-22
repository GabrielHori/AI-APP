# FastAPI main application entry point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.hardware import router as hardware_router
from app.api.gpu import router as gpu_router
from app.api.system import router as system_router
from app.api.models import router as models_router
from app.api.monitoring import router as monitoring_router




app = FastAPI(
    title="AI Launcher Backend",
    version="1.0.0"
)

# Autoriser le frontend (Electron)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hardware_router)
app.include_router(gpu_router)
app.include_router(system_router)
app.include_router(models_router)
app.include_router(monitoring_router)


@app.get("/")
def root():
    return {"status": "Backend is running"}
from app.services.gpu_service import get_gpu_info
from app.services.system_service import get_system_info
from app.data.models_db import MODELS


def check_models_compatibility():
    gpu = get_gpu_info()
    system = get_system_info()

    results = []

    for model in MODELS:
        status = "compatible"
        reasons = []

        if not gpu.get("gpu_available"):
            status = "incompatible"
            reasons.append("No GPU detected")

        if gpu.get("vram_total_mb", 0) / 1024 < model["min_vram"]:
            status = "incompatible"
            reasons.append("Not enough VRAM")

        if system["ram"]["total_gb"] < model["min_ram"]:
            status = "incompatible"
            reasons.append("Not enough RAM")

        if system["cpu"]["threads"] < model["min_threads"]:
            status = "incompatible"
            reasons.append("Not enough CPU threads")

        results.append({
            "model": model["name"],
            "status": status,
            "reasons": reasons,
        })

    return results

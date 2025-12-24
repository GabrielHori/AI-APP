import pynvml as nvml
from typing import Dict, Any

class GPUService:
    def __init__(self):
        self.available = False
        try:
            nvml.nvmlInit()
            self.device_count = nvml.nvmlDeviceGetCount()
            self.available = True
        except Exception as e:
            print(f"Service GPU non disponible : {e}")

    def get_gpu_stats(self) -> Dict[str, Any]:
        if not self.available:
            return {
                "available": False,
                "name": "Aucune détectée",
                "usage": 0,
                "used_mb": 0,
                "total_mb": 0
            }

        try:
            handle = nvml.nvmlDeviceGetHandleByIndex(0)
            
            # === CORRECTION ICI : Compatible Ancienne et Nouvelle Version ===
            name_raw = nvml.nvmlDeviceGetName(handle)
            name = name_raw.decode("utf-8") if isinstance(name_raw, bytes) else name_raw
            # =======================================================

            # Utilisation (%)
            utilization = nvml.nvmlDeviceGetUtilizationRates(handle)
            gpu_usage = utilization.gpu
            
            # Mémoire VRAM
            mem_info = nvml.nvmlDeviceGetMemoryInfo(handle)
            used_mb = mem_info.used // 1024**2
            total_mb = mem_info.total // 1024**2

            return {
                "available": True,
                "name": name,
                "usage": gpu_usage,
                "used_mb": used_mb,
                "total_mb": total_mb
            }

        except Exception as e:
            print(f"Erreur lecture GPU : {e}")
            return { "available": False, "name": "Erreur lecture" }

# Singleton
gpu_service = GPUService()
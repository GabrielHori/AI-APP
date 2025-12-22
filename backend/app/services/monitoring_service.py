import psutil
from pynvml import (
    nvmlInit,
    nvmlShutdown,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetUtilizationRates,
    nvmlDeviceGetMemoryInfo,
    nvmlDeviceGetTemperature,
    NVML_TEMPERATURE_GPU,
)


def get_monitoring_info():
    cpu_percent = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()

    gpu_data = {
        "available": False
    }

    try:
        nvmlInit()
        handle = nvmlDeviceGetHandleByIndex(0)

        utilization = nvmlDeviceGetUtilizationRates(handle)
        mem_info = nvmlDeviceGetMemoryInfo(handle)
        temperature = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)

        gpu_data = {
            "available": True,
            "usage_percent": utilization.gpu,
            "vram_used_mb": mem_info.used // (1024 * 1024),
            "vram_total_mb": mem_info.total // (1024 * 1024),
            "temperature_c": temperature,
        }

    except Exception:
        pass

    finally:
        try:
            nvmlShutdown()
        except Exception:
            pass

    return {
        "cpu": {
            "usage_percent": cpu_percent,
        },
        "ram": {
            "usage_percent": ram.percent,
        },
        "gpu": gpu_data,
    }

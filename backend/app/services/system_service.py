import platform
import psutil


def get_system_info():
    cpu_freq = psutil.cpu_freq()

    return {
        "cpu": {
            "name": platform.processor(),
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "frequency_mhz": int(cpu_freq.max) if cpu_freq else None,
        },
        "ram": {
            "total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
            "available_gb": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        },
    }

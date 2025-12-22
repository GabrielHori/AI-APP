import platform
import psutil


def get_hardware_info() -> dict:
    cpu_freq = psutil.cpu_freq()
    ram = psutil.virtual_memory()

    return {
        "os": {
            "name": platform.system(),
            "version": platform.version(),
            "release": platform.release()
        },
        "cpu": {
            "name": platform.processor(),
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "frequency_mhz": cpu_freq.max if cpu_freq else None
        },
        "ram": {
            "total_gb": round(ram.total / (1024 ** 3), 2),
            "available_gb": round(ram.available / (1024 ** 3), 2)
        }
    }

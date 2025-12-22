from pynvml import (
    nvmlInit,
    nvmlShutdown,
    nvmlDeviceGetCount,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetName,
    nvmlDeviceGetMemoryInfo,
    nvmlSystemGetDriverVersion,
)


def _to_str(value):
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return value


def get_gpu_info():
    try:
        nvmlInit()

        device_count = nvmlDeviceGetCount()
        if device_count == 0:
            return {"gpu_available": False}

        handle = nvmlDeviceGetHandleByIndex(0)

        name = _to_str(nvmlDeviceGetName(handle))
        mem_info = nvmlDeviceGetMemoryInfo(handle)
        driver_version = _to_str(nvmlSystemGetDriverVersion())

        return {
            "gpu_available": True,
            "name": name,
            "vram_total_mb": mem_info.total // (1024 * 1024),
            "driver_version": driver_version,
        }

    except Exception as e:
        return {
            "gpu_available": False,
            "error": str(e),
        }

    finally:
        try:
            nvmlShutdown()
        except Exception:
            pass

import shutil
import psutil
import os
from typing import Dict, Any

class HardwareService:

    def get_system_stats(self) -> Dict[str, Any]:
        """
        Récupère l'état actuel du système.
        Renvoie des valeurs simples (nombres), pas d'objets imbriqués.
        """
        # 1. CPU
        cpu_usage = psutil.cpu_percent(interval=0.1)
        
        # 2. RAM
        mem = psutil.virtual_memory()
        ram_usage = mem.percent
        ram_total_gb = round(mem.total / (1024**3), 2)
        ram_used_gb = round(mem.used / (1024**3), 2)

        # 3. Disque (C:)
        try:
            disk_path = os.getenv('SystemDrive', 'C:')
            disk = shutil.disk_usage(disk_path)
            disk_usage = round((disk.used / disk.total) * 100, 2)
            disk_total_gb = round(disk.total / (1024**3), 2)
        except Exception as e:
            print(f"Erreur disque: {e}")
            disk_usage = 0
            disk_total_gb = 0

        # On retourne tout à plat pour éviter les erreurs React
        return {
            "cpu": cpu_usage,
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "ram_percent": ram_usage,
            "ram_used": ram_used_gb,
            "ram_total": ram_total_gb,
            "disk_percent": disk_usage,
            "disk_total": disk_total_gb
        }

# Singleton
hardware_service = HardwareService()
import httpx
import logging
from typing import List, Dict, Any, Optional

# Configuration simple pour V1
OLLAMA_BASE_URL = "http://localhost:11434"

logger = logging.getLogger(__name__)

class OllamaService:
    def __init__(self):
        self.base_url = OLLAMA_BASE_URL
        # Timeout généreux pour le chargement des modèles lourds
        self.timeout = httpx.Timeout(30.0, connect=10.0)

    async def list_models(self) -> List[Dict[str, Any]]:
        """
        Récupère la liste des modèles disponibles auprès du démon Ollama local.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response.raise_for_status()
                data = response.json()
                
                return data.get("models", [])
                
        except httpx.ConnectError:
            logger.error("Impossible de se connecter à Ollama. Est-il lancé ?")
            return []
        except Exception as e:
            logger.exception(f"Erreur lors de la récupération des modèles: {e}")
            return []

    async def check_connection(self) -> bool:
        """Vérifie rapidement si Ollama est joignable."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                return response.status_code == 200
        except Exception:
            return False

    async def chat(self, model_name: str, prompt: str, history: list = None) -> str:
        """
        Envoie un prompt à Ollama et retourne la réponse de l'IA.
        """
        url = f"{self.base_url}/api/chat"
        
        # Construction du payload pour Ollama
        payload = {
            "model": model_name,
            "stream": False, # Pour V1, on désactive le streaming pour simplifier
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        # Note : L'historique pourra être ajouté ici pour la V2
        # if history: payload["messages"] = history + payload["messages"]

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                data = response.json()
                
                # La réponse d'Ollama est dans le champ "message" -> "content"
                return data.get("message", {}).get("content", "Erreur: Pas de réponse du modèle.")
                
        except httpx.ConnectError:
            logger.error("Erreur de connexion à Ollama lors du chat.")
            return "Erreur: Impossible de contacter Ollama."
        except Exception as e:
            logger.exception(f"Erreur lors du chat: {e}")
            return f"Erreur: {str(e)}"

# Singleton simple pour l'injection de dépendances
ollama_service = OllamaService()
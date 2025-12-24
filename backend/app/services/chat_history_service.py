import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import uuid

# Chemin vers le dossier data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CONVERSATIONS_FILE = os.path.join(DATA_DIR, 'conversations.json')

class ChatHistoryService:
    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        # Créer le fichier s'il n'existe pas
        if not os.path.exists(CONVERSATIONS_FILE):
            self._save_all([])

    def _load_all(self) -> List[Dict]:
        """Charge toutes les conversations."""
        if not os.path.exists(CONVERSATIONS_FILE):
            return []
        try:
            with open(CONVERSATIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def _save_all(self, data: List[Dict]):
        """Sauvegarde toute la liste."""
        with open(CONVERSATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_all_conversations(self) -> List[Dict]:
        """
        Retourne la liste des conversations (ID, Titre, Date, Model).
        Pour l'affichage de la sidebar.
        """
        chats = self._load_all()
        # On trie par date décroissante (plus récent en haut)
        return sorted(chats, key=lambda x: x.get('updated_at', ''), reverse=True)

    def get_conversation_messages(self, chat_id: str) -> Optional[List[Dict]]:
        """Récupère les messages d'une conversation spécifique."""
        chats = self._load_all()
        chat = next((c for c in chats if c['id'] == chat_id), None)
        if chat:
            return chat.get('messages', [])
        return None

    def create_conversation(self, first_prompt: str, model: str) -> str:
        """
        Crée une nouvelle conversation avec le premier message utilisateur.
        Retourne l'ID de la nouvelle conversation.
        """
        new_chat = {
            "id": str(uuid.uuid4()),
            "title": first_prompt[:30] + ("..." if len(first_prompt) > 30 else ""), # Titre = début du prompt
            "model": model,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "messages": [
                {"role": "user", "content": first_prompt, "timestamp": datetime.now().isoformat()}
            ]
        }
        chats = self._load_all()
        chats.append(new_chat)
        self._save_all(chats)
        return new_chat['id']

    def add_message(self, chat_id: str, role: str, content: str):
        """
        Ajoute une réponse (user ou assistant) à une conversation existante.
        Met à jour la date de modification.
        """
        chats = self._load_all()
        chat = next((c for c in chats if c['id'] == chat_id), None)
        if chat:
            chat['messages'].append({
                "role": role, 
                "content": content, 
                "timestamp": datetime.now().isoformat()
            })
            chat['updated_at'] = datetime.now().isoformat()
            self._save_all(chats)

    def delete_conversation(self, chat_id: str):
        """Supprime une conversation."""
        chats = self._load_all()
        chats = [c for c in chats if c['id'] != chat_id]
        self._save_all(chats)

# Singleton
chat_history_service = ChatHistoryService()
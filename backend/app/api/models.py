from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.services.ollama_service import ollama_service
from app.services.chat_history_service import chat_history_service

router = APIRouter()

class ChatRequest(BaseModel):
    model: str
    prompt: str

# --- ROUTES CHAT ---

# ... imports existants ...

class ChatRequest(BaseModel):
    model: str
    prompt: str
    chat_id: Optional[str] = None # On peut passer l'ID de la conversation

@router.post("/chat")
async def chat_with_model(request: ChatRequest):
    """
    Endpoint pour envoyer un message.
    Si chat_id est fourni, on ajoute à la conversation existante.
    Sinon, pour l'instant on ne sauvegarde pas dans l'historique (le Frontend créera une session au premier message).
    """
    # Si chat_id est présent, on sauvegarde le message utilisateur
    if request.chat_id:
        chat_history_service.add_message(request.chat_id, "user", request.prompt)

    # Génération de la réponse IA
    response_content = await ollama_service.chat(
        model_name=request.model, 
        prompt=request.prompt
    )

    # Si chat_id présent, on sauvegarde la réponse IA
    if request.chat_id:
        chat_history_service.add_message(request.chat_id, "assistant", response_content)
    
    return {
        "model": request.model,
        "response": response_content,
        "chat_id": request.chat_id
    }

# Nouvelle route pour la liste des conversations (sidebar)
@router.get("/conversations")
async def get_conversations():
    return chat_history_service.get_all_conversations()

# Route pour récupérer les messages d'un chat spécifique (quand on clique dessus)
@router.get("/conversations/{chat_id}/messages")
async def get_conversation_messages(chat_id: str):
    messages = chat_history_service.get_conversation_messages(chat_id)
    if messages is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return messages

# Route supprimer un chat
@router.delete("/conversations/{chat_id}")
async def delete_conversation(chat_id: str):
    chat_history_service.delete_conversation(chat_id)
    return {"status": "deleted"}

# Route Créer un chat (Premier message)
@router.post("/conversations")
async def create_chat(request: ChatRequest):
    """Crée une nouvelle conversation avec le premier message."""
    chat_id = chat_history_service.create_conversation(request.prompt, request.model)
    
    # Ensuite on génère la réponse
    response_content = await ollama_service.chat(
        model_name=request.model, 
        prompt=request.prompt
    )
    
    chat_history_service.add_message(chat_id, "assistant", response_content)
    
    return {
        "chat_id": chat_id,
        "model": request.model,
        "response": response_content
    }


# --- ROUTES MODELS (Déjà existantes) ---

@router.get("/models", response_model=List[Dict[str, Any]])
async def get_models():
    models = await ollama_service.list_models()
    return models

@router.get("/models/status")
async def get_status():
    is_online = await ollama_service.check_connection()
    return {"status": "online" if is_online else "offline"}
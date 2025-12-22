# Application configuration
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "V1-IA-APP Backend"
    APP_VERSION: str = "1.0.0"
    
    # CORS settings
    CORS_ORIGINS: list = ["http://localhost", "http://localhost:3000"]
    
    # Ollama settings
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_DEFAULT_MODEL: str = "llama3"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Initialize settings
settings = Settings()
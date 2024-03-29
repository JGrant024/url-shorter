import os
from dotenv import load_dotenv
from pathlib import Path
# look in current directory for .env path 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "url-shorter"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : int = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DATABASE : str = os.getenv("POSTGRES_DATABASE","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
    SECRET_KEY: str = os.getenv("SECRET_KEY") 
    

settings = Settings()
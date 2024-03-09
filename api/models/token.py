from datetime import datetime, timedelta, timezone 
from pydantic import BaseModel 
from config import settings
import jwt 

class Token(BaseModel): 
    access_token: str 
    token_type: str = "bearer" 

class TokenData(BaseModel): 
    email: str

def create_access_token(data: dict, expires_delta: timedelta): 
    to_encode = data.copy() 

    if expires_delta: 
        expire = datetime.now(timezone.utc) + expires_delta 
    else: 
        expire = datetime.now(timezone.utc) + timedelta(minutes=15) 
    
    to_encode.update({"exp": expire })
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

    
        

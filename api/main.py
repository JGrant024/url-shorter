from fastapi import FastAPI, HTTPException, Depends, status, Query ;
from fastapi.responses import JSONResponse; 
from fastapi.middleware.cors import CORSMiddleware; 
from sqlalchemy.exc import IntegrityError
from models.links import Links, LinksSchema 
from database.db import engine, session 
from models.token import Token, TokenData, create_access_token
from models.base import Base 
from models.users import User, UserAccountSchema, UserSchema
from config import settings 
from services import create_user, get_user
from datetime import timedelta, date
from starlette.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_tables(): 
    Base.metadata.create_all(bind=engine) 

def start_application(): 
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION); 
    create_tables()
    return app

app = start_application() 


origins = [
    "http://localhost:*", 
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True, 
    allow_methods =["*"], 
    allow_headers = ["*"]
)

@app.get("/")
def home(): 
    return{"message:" "Root Route For Url-Shorter App "}

@app.get("/links")
def get_links():
    links = session.query(Links)
    return links.all()

@app.post("/links/add")
def add_link(link_data: LinksSchema):
    link = Links(**link_data.model_dump())
    print(link)
    session.add(link)
    session.commit()
    return {"Link added": link.title}

@app.post("/register", response_model=UserSchema)
def register_user(payload: UserAccountSchema): 
    payload.hashed_password = User.hash_password(payload.hashed_password)
    return create_user(user=payload) 

@app.post("/login")
async def login(payload: UserAccountSchema): 
    try: 
        user: User = get_user(email=payload.email) 
    except: 
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User Credentials"
        )
    print(payload)
    is_validated: bool = user.validate_password(payload.hashed_password)

    if not is_validated: 
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User Credentials" 
        )
    access_token_expires = timedelta(minutes=120)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get('/logout', status_code=200)
def logout(token: Token = Depends(oauth2_scheme)):  
        session.add(token)
        session.commit()
        return {"details:": "Logged out"}

@app.get("/sendit") 
async def redirect_to_external_url(url: str = Query(...)): 
    link = session.query(Links).filter(Links.short_url == url).first() 

    long_url = f"https://{link.long_url}"  

    return RedirectResponse(long_url) 





    

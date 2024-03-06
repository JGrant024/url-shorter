from fastapi import FastAPI;
from fastapi.responses import JSONResponse; 
from fastapi.middleware.cors import CORSMiddleware; 
from models.links import Links, LinksSchema 
from database.db import engine, session 
from models.base import Base 
from models.users import User, UserAccountSchema, UserSchema
from config import settings 
from services import create_user

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



    

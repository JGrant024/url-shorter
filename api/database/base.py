from database.session import engine
from database.base import Base    
from database.models.user import User 
from database.models.blog import Blog   
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="localhost",
    database="url-shorter",
)


def create_tables(): 
    Base.metadata.create_all(bind=engine) 



engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

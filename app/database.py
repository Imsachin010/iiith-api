from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.log import Base

DATABASE_URL = "sqlite:///./logs.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the logs table
def init_db():
    Base.metadata.create_all(bind=engine)

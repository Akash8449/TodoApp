from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base   

DATABASE_URL = "postgresql://postgres:akash%4024@localhost/todo_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # This will create all tables defined in Base
    Base.metadata.create_all(bind=engine)

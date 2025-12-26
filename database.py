from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Shekhar%402004@localhost:5432/mydatabase"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush= False, bind = engine)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/FIVER"
engine = create_engine(DATABASE_URL,pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
session1 = SessionLocal()
session2 = SessionLocal()
session3 = SessionLocal()
Base = declarative_base()   
from sqlalchemy import create_engine, Column, String, Integer
from models.database import Base

class Log(Base):
    __tablename__ = "Log"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    route = Column(String, nullable=False)  # To store the route as a string
    status = Column(Integer, nullable=False)  # To store the status code
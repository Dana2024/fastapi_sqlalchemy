from sqlalchemy import Column, Integer, String
from database import Base

class Flavors(Base):
    __tablename__ = "flavors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
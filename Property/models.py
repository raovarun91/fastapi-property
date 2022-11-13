from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class Prop(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    bed_rooms = Column(Integer)
    rent = Column(Integer)
    location = Column(String)
    rented = Column(Boolean, default=True)
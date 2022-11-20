from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Prop(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    bed_rooms = Column(Integer)
    rent = Column(Integer)
    location = Column(String)
    rented = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship('User', back_populates="property")

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    property = relationship('Prop', back_populates="creator")
from pydantic import BaseModel
from typing import Optional, List

class PropBase(BaseModel):
    name:str
    bed_rooms:int
    rent:int
    location:str
    rented: Optional[bool]

class Prop(PropBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email: str
    password: str

class ShowUser(BaseModel):
    name:str
    email: str
    class Config():
        orm_mode = True

class ShowUserId(ShowUser):
    property: List[Prop] = []
    class Config():
        orm_mode = True    

class ShowProp(BaseModel):
    name:str
    bed_rooms:int
    rent:int
    class Config():
        orm_mode= True

class ShowCompleteProp(Prop):
    creator: ShowUser
    class Config():
        orm_mode = True


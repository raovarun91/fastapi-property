from pydantic import BaseModel
from typing import Optional

class Prop(BaseModel):
    name:str
    bed_rooms:int
    rent:int
    location:str
    rented: Optional[bool]
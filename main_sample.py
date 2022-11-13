from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, reload=True)

@app.get('/')
def home():
    return {"data" :"This is the home page of the API. This Api will list Properties for Rent."}

@app.get('/help')
def help():
    return "This return the help section for the API"

@app.get('/property')
def proterty_all(limit, rented=False, sort: Optional[str]=None):
    "Rented Properties are not displayed here"
    if rented:
        return f"Propert Details for first {limit}"
    else:
        return f"Propert Details for first unrented {limit}"

@app.get('/property/{id}')
def proterty_details(id: int):
    return f"Propert Details {id}"

class Property(BaseModel):
    name:str
    bed_rooms:int
    rent:int
    location:str
    rented: Optional[bool]


@app.post('/create_property')
def create_property(property:Property):
    return property

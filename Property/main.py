# from Main import Property

from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app =FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/property', status_code=status.HTTP_201_CREATED)
def create_property(prop:schemas.Prop, db: Session = Depends(get_db)):
    new_prop = models.Prop(name = prop.name, bed_rooms =prop.bed_rooms, 
                            rent=prop.rent, location=prop.location,
                            rented = prop.rented)
    db.add(new_prop)
    db.commit()
    db.refresh(new_prop)
    return new_prop

@app.get('/property')
def all(db: Session = Depends(get_db)):
    props = db.query(models.Prop).all()
    return props

@app.get('/property/{ids}', status_code =200)
def show(ids, response:Response, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == ids).first()
    if not prop:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Blog number {ids} is not available'}
    return prop

@app.put('/property/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, response:schemas.Prop, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == id)
    if not prop.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
            detail= f'Blog number {id} is not available')        
    prop.update(response.dict())
    db.commit()
    return 'updated'


@app.delete('/property/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == 
                                    id).delete(synchronize_session=False)
    db.commit()
    return "blog deleted"


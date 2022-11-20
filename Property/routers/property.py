from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/property',
    tags = ["Property"]
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_property(prop:schemas.Prop, db: Session = Depends(get_db)):
    new_prop = models.Prop(name = prop.name, bed_rooms =prop.bed_rooms, 
                            rent=prop.rent, location=prop.location,
                            rented = prop.rented, user_id=1)
    db.add(new_prop)
    db.commit()
    db.refresh(new_prop)
    return new_prop

@router.get('/', response_model=List[schemas.ShowProp])
def all(db: Session = Depends(get_db)):
    props = db.query(models.Prop).all()
    return props

@router.get('/{ids}', status_code =200, response_model=schemas.ShowCompleteProp)
def show(ids, response:Response, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == ids).first()
    if not prop:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Blog number {ids} is not available'}
    return prop

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, response:schemas.Prop, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == id)
    if not prop.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
            detail= f'Blog number {id} is not available')        
    prop.update(response.dict())
    db.commit()
    return 'updated'

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    prop = db.query(models.Prop).filter(models.Prop.id == 
                                    id).delete(synchronize_session=False)
    db.commit()
    return "blog deleted"

from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from .. import schemas, database, models
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name= request.name, email=request.email, 
                        password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.ShowUserId)
def user(id: int, response:Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                detail= f"Failed to find user id - {id}")
    return user
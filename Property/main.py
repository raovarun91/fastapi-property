# from Main import Property
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import property, user


app =FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(property.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/property', status_code=status.HTTP_201_CREATED, tags=['Property'])
# def create_property(prop:schemas.Prop, db: Session = Depends(get_db)):
#     new_prop = models.Prop(name = prop.name, bed_rooms =prop.bed_rooms, 
#                             rent=prop.rent, location=prop.location,
#                             rented = prop.rented, user_id=1)
#     db.add(new_prop)
#     db.commit()
#     db.refresh(new_prop)
#     return new_prop

# @app.get('/property', response_model=List[schemas.ShowProp], tags=['Property'])
# def all(db: Session = Depends(get_db)):
#     props = db.query(models.Prop).all()
#     return props

# @app.get('/property/{ids}', status_code =200, response_model=schemas.ShowCompleteProp, tags=['Property'])
# def show(ids, response:Response, db: Session = Depends(get_db)):
#     prop = db.query(models.Prop).filter(models.Prop.id == ids).first()
#     if not prop:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'detail': f'Blog number {ids} is not available'}
#     return prop

# @app.put('/property/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Property'])
# def update(id, response:schemas.Prop, db: Session = Depends(get_db)):
#     prop = db.query(models.Prop).filter(models.Prop.id == id)
#     if not prop.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
#             detail= f'Blog number {id} is not available')        
#     prop.update(response.dict())
#     db.commit()
#     return 'updated'


# @app.delete('/property/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Property'])
# def delete(id, db: Session = Depends(get_db)):
#     prop = db.query(models.Prop).filter(models.Prop.id == 
#                                     id).delete(synchronize_session=False)
#     db.commit()
#     return "blog deleted"


# User section of the code

# @app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=['User'])
# def create_user(request:schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name= request.name, email=request.email, 
#                         password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model=schemas.ShowUserId, tags=['User'])
# def user(id: int, response:Response, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#                 detail= f"Failed to find user id - {id}")
#     return user


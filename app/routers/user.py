from fastapi import APIRouter
from ..import schemas, database
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


# function to create a new user
@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

# function to get all users
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get(id, db)
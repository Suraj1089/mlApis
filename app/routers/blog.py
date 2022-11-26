from fastapi import APIRouter
from ..import schemas, database
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, status
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_blog(id, db: Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(database.get_db)):
    blog.destroy(id, db)


def update_blog(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    """
    User class to store user data
    """
    __tablename = 'users'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    items = relationship("Item",back_populates="owner")


class Item(Base):
    """
    Item class to store item data
    """
    __tablename__ = 'items'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String,index=True)
    owner_id = Column(Integer,ForeignKey('users.id'))


    owner = relationship("User",back_populates="items")

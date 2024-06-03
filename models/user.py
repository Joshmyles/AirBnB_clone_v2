#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class 
    Attributes:
        first_name -- first name
        last_name -- last name
        email -- email
        password -- password
    """

    __tablename__ = "users"
    first_name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    places = relationship(
        "Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship(
        "Review", cascade='all, delete, delete-orphan', backref="user")

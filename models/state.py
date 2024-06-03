#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import models
import shlex


class State(BaseModel, Base):
    """ State class 

    Attributes:
        name: name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete delete-orphan", backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        my_list = []
        result = []
        for key in var:
            city = key.replace('.', '')
            city = shlex.split(city)
            if (city[0] == 'city'):
                my_list.append(var[key])
        for element in my_list:
            if (element.state_id == self.id):
                result.append(element)
        return (result)

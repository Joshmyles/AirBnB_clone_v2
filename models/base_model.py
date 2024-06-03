#!/usr/bin/python3
"""This module defines a base class for all models in hbnb project"""
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

import uuid
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models (common attributes and methods)"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=(datetime.now(datetime.utc)))
    updated_at = Column(DateTime, nullable=False,
                        default=(datetime.now(datetime.utc)))

    def __init__(self, *args, **kwargs):
        """Instantiation of base model

        Args:
            args -- not used
            kwargs -- used by the constructor of the BaseModel
        Attributes:
            id: unique id
            created_at: date of creation
            updated_at: date of last update
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance

        Return: a string of class name, id and dictionary
        """
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """returns a string representation"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates a dictionary of the class

        Return: a dictionary containing key values in __dict__
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """"Delete an object"""
        models.storage.delete(self)

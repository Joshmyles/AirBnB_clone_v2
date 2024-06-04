#!/usr/bin/python3
"""File storage module for HBNB Project"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json
import shlex


class FileStorage:
    """serializes instances to a JSON file, deserialized JSON file to instances

    Attributes:
        __file_path -- path to JSON file
        __objects -- objects to be stored
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage

        Return: 
            a dictionary of __objects
        """
        _dict = {}
        if cls:
            my_dict = self.__objects
            for key in my_dict:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    _dict[key] = self.__objects[key]
            return (_dict)
        else:
            return self.__objects

    def new(self, obj):
        """sets __objects to given obj

        Args:
            obj: object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize file path to JSON file path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete an existing object"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """"call reload"""
        self.reload()

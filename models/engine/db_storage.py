"""DB storage module for HBNB Project"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """"DB Storage Class

    Attributes:
        __engine = None
        __session = None
    """

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """dictionary

        Return: returns a dictionary of __objects
        """
        __dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                __dict[key] = element
        else:
            __list = [State, City, User, Place, Review, Amenity]
            for i in __list:
                query = self.__session.query(i)
                for element in query:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    __dict[key] = element
        return (__dict)

    def new(self, obj):
        """"Add a new field in the table"""
        self.__session.add(obj)

    def save(self):
        """"Save Changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """"Delete a field in the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """"Configurations"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """"For removing session"""
        self.__session.close()

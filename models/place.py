#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """ A place to stay """

    def __init__(self, *args, **kwargs):
        """"initialization instance"""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.longitude = 0.0
        self.latitude = 0.0
        self.amenity_ids = []

    city_id = str  # id of city where the place is located
    user_id = str  # id of user who owns the place
    name = str  # name of the place
    description = str  # description of the place
    number_rooms = int  # number of rooms in the place
    number_bathrooms = int  # number of bathrooms in the place
    max_guest = int  # max number of guests the place can hold
    price_by_night = int  # price of the place per night
    latitude = float  # lat coordinates of the place
    longitude = float  # log coordinates of the place
    # list of ids of the amenities that the place offers
    amenity_ids = List[str]

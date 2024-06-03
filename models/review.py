#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that stores review information """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    place_id = str  # id of the place being reviewed
    user_id = str  # id of the user reviewing the place
    text = str  # information of the review

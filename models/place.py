#!/usr/bin/python3
"""Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place
    Attributes:
    City id
    User id
    Name of the place
    Description of the place
    Number of rooms of the place
    Number of bathrooms of the place
    Maximum number of guests of the place
    Price by night of the place
    Latitude of the place
    Longitude of the place
    List of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

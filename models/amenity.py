#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity
    Attributes:
    name (str) name of the amenity
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)

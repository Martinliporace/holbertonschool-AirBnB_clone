#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User
    Attributes:
    email + password + first name +
    last name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)

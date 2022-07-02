#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel
import models

class User(BaseModel):
    """Represent a User Attributes:
    email + password + first name +
    last name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)

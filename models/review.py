#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    Attributes:
    Place id
    User id
    Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)

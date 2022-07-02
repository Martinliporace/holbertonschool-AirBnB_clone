#!/usr/bin/python3
"""State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state
    Attributes:
        name (str)"""


    name = ""

    
    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""Base class"""

import json
import uuid
import datetime
import time

class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, id=None, created_at, updated_at):
        """init"""

        self.id = id
        if self.id is None:
            self.id = str(uuid.uuid4())
        self.created_at = Date()
        self.updated_at = Date()
        print("id", self.id)

    def Date(self):
        Date = datetime.datetime.now()
        DateTime_in_ISOFormat = Date.isoformat()
        return(str(DateTime_in_ISOFormat))

    def __str__(self):
        return("[BaseModel] ({})".format(self.id))

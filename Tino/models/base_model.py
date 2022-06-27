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

    def __init__(self):
        """init"""

        self.id = str(uuid.uuid4())
        self.created_at = str(BaseModel.Date(self))
        self.updated_at = str(BaseModel.Date(self))
        print("id", self.id)

    def Date(self):
        Date = datetime.datetime.now()
        DateTime_in_ISOFormat = Date.isoformat()
        return(DateTime_in_ISOFormat)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
    def save(self):
        self.updated_at = str(BaseModel.Date(self))

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at
        dic["updated_at"] = self.updated_at
        dic["__class__"] = self.__class__.__name__
        return dic
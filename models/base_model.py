#!/usr/bin/python3
"""Base class"""

import json
import uuid
from datetime import datetime
import time


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialize the class constructor"""

        if kwargs:
            dtf = "%Y-%m-%dT%H:%M:%S.%f"
            for keys, values in kwargs.items():
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        values = datetime.strptime(values, dtf)
                    setattr(self, keys, values)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

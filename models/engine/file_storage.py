#!/usr/bin/python3
"""FileStorage class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        str = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(str, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        odict = FileStorage.__objects
        aux = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(aux, f)

    def reload(self):
        """Deserialize the JSON to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                aux = json.load(f)
                for o in aux.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

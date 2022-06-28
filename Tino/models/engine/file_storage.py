#!/usr/bin/python3
"""FileStorage class"""

import json
from models.base_model import BaseModel
from os import path


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return(self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[(str(obj.__class__.__name__)) + '.' + (str(obj.id))] = obj

    def save(self):
        """serializes __objects to the JSON file (path: self.__file_path)"""
        aux = {}
        for keys, values in self.__objects.items():
            aux[keys] = values.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(aux, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as json_file:
                obj = json.load(json_file)
        except FileNotFoundError:
            pass
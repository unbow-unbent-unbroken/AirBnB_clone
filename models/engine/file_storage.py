#!/usr/bin/python3
"""Defines a new class called FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns  the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        # k = str(obj.__class__.__name__) + '.' + str(obj.id)
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        my_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return

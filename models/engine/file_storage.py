#!/usr/bin/python3
"""
This module defines a class Filetorage that serializes instances to a JSON
file and deserializes JSON file to instances.

Class:
    FileStorage: Serializes instances to a JSON file and deserializes JSON
    file to instances..

Attributes:
    class_list: List of classes in program

Functions:
    None
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }


class FileStorage:
    """
    Class serializes instances to JSON file and deserializes JSON to
    instances.

    Attributes:
        __file_path (str): Path to JSON file (class attr)
        __objects (dict): Stores objects by "<class name>.id" (class attr)

    Methods:
        all: Returns the dictionary __objects
        new(obj): Sets in __objects the obj with key '<obj class name>.id'
        save: Serializes __objects to the JSON file
        reload: Deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects that stores objects by class name
        and id.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the object with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key, value in
                      self.__objects.items()}, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                # Store each object in __objects
                for key, obj in loaded_objects.items():
                    class_name = obj['__class__']
                    self.__objects[key] = class_list[class_name](**obj)
        # Do nothing if the file doesn't exist
        except (FileNotFoundError):
            pass

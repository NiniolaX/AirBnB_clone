#!/usr/bin/python3

"""This module defines a class fileStorage
This class serializes instances to a JSON file and
also deserializes JSON file to instances
"""

import models
from models.base_model import BaseModel
import json
import os  # this is needed to verify if file exist
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# create a list of classes
class_list = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class FileStorage:

    """ Serializes and Deserializes instances to JSON file
    and JSON file to instances respectively
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):

        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):

        """serializes __objects to the JSON file (path: __file_path)"""
        # open the file for serialization (write mode)
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()},
                      file, default=str)

    def reload(self):

        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        else, do nothing.
        If the file doesn't exist, no exception should be raised
        """

        # check if path exists, if true open the file for decoding
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as file:
                    loaded_objects = json.load(file)
                    # convert loaded objects to instances of BaseModel
                for key, value in loaded_objects.items():
                    # retrieve class name from dict (value)
                    class_name = value.get('__class__')
                    if class_name in class_list:
                        new_instance = class_list[class_name](**value)
                        self.__objects[key] = new_instance
            except Exception as e:
                pass
        else:
            pass

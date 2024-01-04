#!/usr/bin/python3
import json
"""
This module defines a class Filetorage that serializes instances to a JSON
file and deserializes JSON file to instances.

Class:
    FileStorage: Serializes instances to a JSON file and deserializes JSON
    file to instances..

Attributes:
    None

Functions:
    None
"""


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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        # Do nothing if the file doesn't exist
        except FileNotFoundError:
            pass

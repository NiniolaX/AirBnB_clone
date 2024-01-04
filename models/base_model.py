#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

"""
This module defines a class BaseModel which defines all common attributes and
methods for other classes.

Class:
    BaseModel: Defines common attributes and methods for other classes.

Attributes:
    None

Functions:
    None
"""


class BaseModel:
    """A class that defines all common attributes and methods for other
    classes.

    Attributes:
        id (uuid.uuid4): Unique identification number of class instances.
        created_at (datetime): Datetime when an instance is created.
        updated_at (datetime): Datetime when an instance was updated.

    Methods:
        __str__(): Returns a string representation of a class instance
        save: Updates the 'updated_at' attribute with the current datetime
        to_dict: Returns a dictionary containing all keys/values of the
                __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """Constructs a new instance of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            # If kwargs is not empty, create BaseModel object from dictionary
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of instance in format:
        "[<class name>] (<self.id>) <self.__dict__>"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        obj_dict = {}
        obj_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            # Convert datetime objects to ISO format
            if key in ['created_at', 'updated_at']:
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict

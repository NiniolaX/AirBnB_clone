#!/usr/bin/python3

import uuid
from datetime import datetime

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

    def __init__(self, **kwargs):
        """Initializes a new instance of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __setattr__(self, name, value):
        """
        Modify setatrr method to update update_at whenever a change is
        made to an instance
        """
        super().__setattr__(name, value)
        if name != 'updated_at':
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of a __dict__ of
        the instance
        """
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict

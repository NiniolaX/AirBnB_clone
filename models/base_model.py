#!/usr/bin/python3
"""
This module defines the class `BaseModel`
This class `BaseModel` would serve as the base class -
for future classes/instances
It defines all common attributes/methods for other classes
"""


from datetime import datetime
import uuid
from . import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ pub. instance attribute: instantiates each instance created"""
        if kwargs:  # if kwargs is not empty, key=attr_name, val=attr_val
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # convert to string
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # add the new instance to storage

    def __str__(self):
        """ returns a string representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the pub instance attr 'updated_at' wt current datetime"""
        self.updated_at = datetime.now()
        # call save method on storage here
        storage.save()

    def to_dict(self):
        """ returns a dict of all key/values of __dict__ of the instance"""
        # start with an empty dictionary
        dict_output = {}

        # use the builtin update() method for dicts to update the dict val
        dict_output.update(self.__dict__)

        # add the key __class__ with class name as value
        dict_output["__class__"] = self.__class__.__name__

        # convert the 'create_at' and 'updated_at' to string ISO format
        if "created_at" in dict_output:
            dict_output["created_at"] = dict_output["created_at"].isoformat()
        if "updated_at" in dict_output:
            dict_output["updated_at"] = dict_output["updated_at"].isoformat()

        # return the dictionary
        return dict_output

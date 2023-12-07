#!/usr/bin/python3
"""
This module defines the class `BaseModel`
This class `BaseModel` would serve as the base class -
for future classes/instances
It defines all common attributes/methods for other classes
"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ pub. instance attribute: instantiates each instance created"""
        if kwargs:  # if kwargs is not empty, key=attr_name, val=attr_val
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(
                                self, key, datetime.strptime
                                (value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # convert to string
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)  # add the new instance to storage

    def __str__(self):
        """ returns a string representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the pub instance attr 'updated_at' wt current datetime"""
        self.updated_at = datetime.now()
        # call save method on storage here
        models.storage.save()

    def to_dict(self):
        """ returns a dict of all key/values of __dict__ of the instance"""
        # start with an empty dictionary
        dict_output = {}

        # add the key __class__ with class name as value
        dict_output["__class__"] = self.__class__.__name__

        # add other key-value paris
        for key, value in self.__dict__.items():
            if key  in ["created_at", "updated_at"]:
                dict_output[key] = value.isoformat()
            else:
                dict_output[key] = value

        # return the dictionary
        return dict_output

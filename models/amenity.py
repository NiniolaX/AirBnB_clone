#!/usr/bin/python3
"""this module defines a class `Amenity`
this class inherits from `BaseModel`
It creates a new amenity objects
while inheriting all properties of `BaseModel`
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """A blueprint for all amenity objects
    it inherits all properties from `BaseModel`
    """
    # create public class attributes
    name = ''

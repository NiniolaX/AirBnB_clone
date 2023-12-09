#!/usr/bin/python3

"""this module defines a class amenity
this class inherits from baseModel
It creates a new amenity objects
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """A blueprint for all amenity objects
    it inherits all properties from baseModel
    """
    # create public class attributes
    name = ''

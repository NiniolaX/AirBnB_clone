#!/usr/bin/python3

"""this module defines a class city
this class inherits from baseModel
It creates a new city objects while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """A blueprint for all city objects
    it inherits all properties from baseModel
    """
    # create public class attributes
    state_id = ''
    name = ''

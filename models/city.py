#!/usr/bin/python3
"""this module defines a class `City`
this class inherits from `BaseModel`
It creates a new city objects while inheriting all properties of `BaseModel`
"""


from models.base_model import BaseModel


class City(BaseModel):
    """A blueprint for all city objects
    it inherits all properties from `BaseModel`
    """
    # create public class attributes
    state_id = ''
    name = ''

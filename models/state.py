#!/usr/bin/python3

"""this module defines a class `State`
this class inherits from `BaseModel`
It creates a new state object while inheriting all properties of `BaseModel`
"""


from models.base_model import BaseModel


class State(BaseModel):

    """A blueprint for all state objects
    it inherits all properties from `BaseModel`
    """
    # create public class attributes
    name = ''

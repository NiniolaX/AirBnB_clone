#!/usr/bin/python3
"""this module defines a class `User`
this class inherits from `BaseModel`
It creates a new user while inheriting all properties of `BaseModel`
"""


from models.base_model import BaseModel


class User(BaseModel):
    """A blueprint for all users objects
    it inherits all properties from `BaseModel`
    """
    # create public class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''

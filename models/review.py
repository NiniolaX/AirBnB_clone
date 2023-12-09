#!/usr/bin/python3
"""this module defines a class `Review`
this class inherits from `BaseModel`
It creates a new review object
while inheriting all properties of `BaseModel`
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """A blueprint for all review objects
    it inherits all properties from `BaseModel`
    """
    # create public class attributes
    place_id = ''
    user_id = ''
    text = ''

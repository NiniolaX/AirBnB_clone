#!/usr/bin/python3

"""this module defines a class review
this class inherits from baseModel
It creates a new review object
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):

    """A blueprint for all review objects
    it inherits all properties from baseModel
    """
    # create public class attributes
    place_id = ''
    user_id = ''
    text = ''

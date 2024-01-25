#!/usr/bin/python3
"""
This module contains a class Review which inherits from BaseModel

Class:
    State: Class from which review objects are created.

Attributes:
    None

Functions:
    None
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class from which review objects are created.

    Attributes:
        place_id(str): Id of place
        user_id(str): Id of user
        text(str): Review content

    Methods:
        None
    """

    place_id = ""
    user_id = ""
    text = ""

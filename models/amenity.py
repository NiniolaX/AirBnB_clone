#!/usr/bin/python3
"""
This module contains a class Amenity which inherits from BaseModel

Class:
    State: Class from which amenity objects are created.

Attributes:
    None

Functions:
    None
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class from which amenity objects are created.

    Attributes:
        name(str): Name of amenity

    Methods:
        None
    """

    name = ""

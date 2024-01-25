#!/usr/bin/python3
"""
This module contains a class City which inherits from BaseModel

Class:
    State: Class from which city objects are created.

Attributes:
    None

Functions:
    None
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class from which city objects are created.

    Attributes:
        state_id(str): Id of state
        name(str): Name of city

    Methods:
        None
    """

    state_id = ""
    name = ""

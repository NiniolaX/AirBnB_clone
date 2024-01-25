#!/usr/bin/python3
"""
This module contains a class State which inherits from BaseModel

Class:
    State: Class from which state objects are created.

Attributes:
    None

Functions:
    None
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class from which state objects are created.

    Attributes:
        name(str): Name of state

    Methods:
        None
    """

    name = ""

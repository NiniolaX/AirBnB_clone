#!/usr/bin/python3
"""
This modules contains the User class which inherits from BaseModel.

Class:
    User: Class from which all User objects inherit.

Attributes:
    None

Functions:
    None
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class from which all 'user' objects inherit.

    Attributes:
        email (str): Email of user
        password (str): Password of user
        first_name (str): First name of user
        last_name (str): Last name of user

    Methods:
        None
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

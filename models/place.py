#!/usr/bin/python3
"""
This module contains a class Place which inherits from BaseModel

Class:
    State: Class from which place objects are created.

Attributes:
    None

Functions:
    None
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class from which place objects are created.

    Attributes:
        city_id(str): Id of city
        user_id(str): Id of user
        name(str): Name of place
        description(str): Description of place
        number_rooms(int): Number of rooms
        number_bathrooms(int): Number of bathrooms
        max_guest(int): Maximum number of guests
        price_by_night(int): Price of place by night
        latitude(float): Latitude of place
        longitude(float): Longitude of place
        amenity_ids(list of str): Ids of amenities

    Methods:
        None
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

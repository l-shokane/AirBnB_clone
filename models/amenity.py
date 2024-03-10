#!/usr/bin/python3
"""Defines the Amenity class from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity of BaseModel.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

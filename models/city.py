#!/usr/bin/python3
"""Defines a City class from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city of BaseModel.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

#!/usr/bin/python3
"""Defines State class from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): Name of the state.
    """

    name = ""

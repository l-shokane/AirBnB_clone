#!/usr/bin/python3
"""Defines all common methods for other classes."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the BaseModel of the hbnb project."""

    def __init__(self, *args, **kwargs):
        """Initializing a new instance/BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timef = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timef)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates the public instance with current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary containing all keys/values."""
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

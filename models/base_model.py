#!/usr/bin/python3
"""Defines base class"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Define the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

            Args:
                args: Variable length argument list.
                kwargs: Arbitrary keyword arguments.
         If kwargs is not provided, use default
        values for id, created_at, and updated_at and
        add the instance to the storage.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                    self.__setattr__(k, v)
                elif k != "__class__":
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        c_dict = self.__dict__.copy()
        c_dict["__class__"] = str(type(self).__name__)
        c_dict["created_at"] = self.created_at.isoformat()
        c_dict["updated_at"] = self.updated_at.isoformat()
        return c_dict

#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.

    Public Class Attributes:
        state_id (str): Empty string.
        name (str): Empty string.
    """
    state_id = ""
    name = ""

#!/usr/bin/python3
"""Review child class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Public Class Attributes:
        place_id (str): Empty string.
        user_id (str): Empty string.
        text (str): Empty string.
    """
    place_id = ""
    user_id = ""
    text = ""

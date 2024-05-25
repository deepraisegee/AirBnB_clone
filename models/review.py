#!/usr/bin/python3
"""
Module for Review model class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model class"""

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""
Module that describe the user model and all reletad functions
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The user model class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

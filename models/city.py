#!/usr/bin/python3
"""
Module for City model class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City model class for location city"""

    state_id = ""
    name = ""

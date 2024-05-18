#!/usr/bin/python3

"""
Decribes all the base model classes to be used for the program
"""
import uuid
from datetime import datetime as dt

from models import storage


class BaseModel(object):
    """
    BaseModel that defines all common attributes
    and amethods for other classes.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop("__class__", "")
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """dictionary representation of the instance"""
        data = self.__dict__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        data["__class__"] = self.__class__.__name__
        return data

    def save(self):
        """save instance state"""
        # update the timestame for the instance modification
        self.updated_at = dt.now()
        storage.save()

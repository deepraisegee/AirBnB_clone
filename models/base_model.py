#!/usr/bin/python3

"""
Decribes all the base model classes to be used for the program
"""
import uuid
from datetime import datetime as dt

import models


class BaseModel(object):
    """
    BaseModel that defines all common attributes
    and amethods for other classes.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop("__class__", "")
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            created_at = kwargs["created_at"]
            updated_at = kwargs["updated_at"]
            kwargs["created_at"] = dt.strptime(created_at, date_format)
            kwargs["updated_at"] = dt.strptime(updated_at, date_format)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """dictionary representation of the instance"""
        data = self.__dict__.copy()  # copy the obj __dict__  property
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        data["__class__"] = self.__class__.__name__
        return data

    def save(self):
        """save instance state"""
        # update the timestame for the instance modification
        self.updated_at = dt.now()
        models.storage.save()

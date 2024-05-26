#!/usr/bin/python3
"""
Module with interfaces for readind and writing
into file to keep the AirBnB data persistence.
"""
import ast
import json
from datetime import datetime as dt

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage(object):
    """
    Storage class that handle the serialization and
    deserialization of JSON data for the instances
    Representation
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """get all the instances"""
        return FileStorage.__objects

    def new(self, obj):
        """create new instance"""
        obj_id = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """save all the objects in the memory to file"""
        data = FileStorage.__objects
        new_data = {k: v.to_dict() for k, v in data.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_data, f, indent=4)

    def reload(self):
        """load the data in the file to memory"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        else:
            FileStorage.__objects = {
                    _id: eval(obj["__class__"])(**obj)
                    for _id, obj in data.items()
                }

    def get(self, obj_id):
        """get instance by its id"""
        return FileStorage.__objects[obj_id]

    def update(self, obj_id, *args, **kwargs):
        """update an instance of `obj_id` with `data`"""
        if kwargs:
            attr = kwargs["attr"]
            val = kwargs["val"]
            if attr not in ("id", "created_at", "updated_at"):
                FileStorage.__objects[obj_id].__dict__[attr] = val
                self.save()
                return
        if args:
            data = ast.literal_eval(args[0])
            FileStorage.__objects[obj_id].__dict__.update(data)
            self.save()

    def delete(self, obj_id):
        """delete an instance from the file storage"""
        FileStorage.__objects.pop(obj_id)
        self.save()

    def filter(self, class_name=None, *args, **kwargs):
        """filter the storage based on params given"""
        results = [
            str(obj) for obj in FileStorage.__objects.values()
        ]
        if class_name is not None:
            results = [
                str(obj) for obj in FileStorage.__objects.values()
                if class_name == obj.__class__.__name__
            ]
        return results

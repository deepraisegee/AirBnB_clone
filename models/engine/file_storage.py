#!/usr/bin/python3
"""
Module with interfaces for readind and writing
into file to keep the AirBnB data persistence.
"""
import json

from models.base_model import BaseModel


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
        FileStorage.__objects[obj_id] = obj.to_dict()

    def save(self):
        """save all the objects in the memory to file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f, indent=4)

    def reload(self):
        """load the data in the file to memory"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                FileStorage.__objects = {
                    _id: eval(obj["__class__"])(**obj).to_dict()
                    for _id, obj in data.items()
                }
        except FileNotFoundError:
            pass

    def get(self, obj_id):
        """get instance by its id"""
        return FileStorage.__objects[obj_id]

    def delete(self, obj_id):
        """delete an instance from the file storage"""
        FileStorage.__objects.pop(obj_id)
        self.save()

    def filter(self, class_name=None, *args, **kwargs):
        """filter the storage based on params given"""
        results = [
            str(eval(obj["__class__"])(**obj))
            for obj in FileStorage.__objects.values()
        ]
        if class_name is not None:
            results = [
                str(eval(obj["__class__"])(**obj))
                for obj in FileStorage.__objects.values()
                if class_name == obj["__class__"]
            ]
        return results

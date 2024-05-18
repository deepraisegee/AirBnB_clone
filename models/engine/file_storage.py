#!/usr/bin/python3
"""
Module with interfaces for readind and writing
into file to keep the AirBnB data persistence.
"""
import json


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
        return self.__objects

    def new(self, obj):
        """create new instance"""
        self.__objects[obj.__class__.__name__] = obj

    def save(self):
        """save all the objects in the memory to file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """load the data in the file to memory"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

CLASSES = {
    "BaseModel": BaseModel
}

storage = FileStorage()
storage.reload()

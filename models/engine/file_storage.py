#!/usr/bin/python3

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import os

"""FileStorage Module that serializes instances to a JSON file
and deserializes JSON file to instances:
"""


class FileStorage:
    """FileStorage class for serializing and deserializing instances
    to/from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary to store objects by class name and id.
    Methods:
        all(self): Returns the dictionary of stored objects.
        new(self, obj): Adds an object to the stored objects.
        save(self): Serializes stored objects to the JSON file.
        reload(self): Deserializes the JSON file to restore stored objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects.
        Returns:
            dict: A dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the stored objects.
        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes stored objects to the JSON file.
        """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(serialized, my_file)

    def reload(self):
        """Deserializes the JSON file to restore stored objects.
        (only if the JSON file (__file_path) exists.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, mode='r') as my_file:
                    FileStorage.__objects = {}
                    data = json.load(my_file)
                for key in data.keys():
                    cls = data[key].pop("__class__", None)
                    cr_at = data[key]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%dT%H:%M:%S.%f")
                    up_at = data[key]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%dT%H:%M:%S.%f")
                    FileStorage.__objects[key] = eval(cls)(data[key])
            except FileNotFoundError:
                pass

#!/usr/bin/python3

import os
import json
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class.
    Attributes:
        file_storage (FileStorage): An instance of FileStorage for testing.
        test_filename (str): The name of the test JSON file
        used during testing.
    Methods:
        setUp(); tearDown();
        test_all(); test_all_with_arg();
        test_new(); test_save();
        test_reload(); test_reload_with_arg();
    """

    def setUp(self):
        """Initializes the FileStorage instance and test file for testing.
        """
        self.file_storage = FileStorage()
        self.test_filename = "test_file.json"

    def tearDown(self):
        """Cleans up any test files created during testing.
        """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_all(self):
        """Test the 'all' method to return the dictionary of stored objects.
        """
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_all_with_arg(self):
        """Test 'all' method with an argument (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test the 'new' method to add an object to the stored objects.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        """Test the 'save' method to serialize stored objects to a JSON file.
        """
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_reload(self):
        """Test the 'reload' method to load objects from a JSON file.
        """
        bm = BaseModel()
        models.storage.new(bm)
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)

    def test_reload_with_arg(self):
        """Test 'reload' method with an argument (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)
	    def test_class_list_unregistered_class(self):
        """Test creating an object for an unregistered class."""
        class_name = "UnregisteredClass"
        data = {"_class_": class_name, "id": "test_id"}
        with open(self.test_filename, "w") as f:
            json.dump({"{}.test_id".format(class_name): data}, f)
        self.file_storage.FileStorage_objects = {}
        self.file_storage.reload()
        self.assertNotIn("{}.test_id".format(class_name), self.file_storage.all())



if __name__ == '__main__':
    unittest.main()

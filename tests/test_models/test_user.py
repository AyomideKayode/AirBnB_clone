#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initialize a User instance for testing"""
        self.user = User()
        self.test_filename = "test_file.json"

    def tearDown(self):
        """Cleans up any test files created during testing.
        """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_attributes(self):
        """Test if the User class has the expected attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_email_default_value(self):
        """Test the default value of the 'email' attribute"""
        self.assertEqual(self.user.email, "")

    def test_password_default_value(self):
        """Test the default value of the 'password' attribute"""
        self.assertEqual(self.user.password, "")

    def test_first_name_default_value(self):
        """Test the default value of the 'first_name' attribute"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_default_value(self):
        """Test the default value of the 'last_name' attribute"""
        self.assertEqual(self.user.last_name, "")

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user), True)


    def test_inheritance(self):
        """Test if User class inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3

"""Unittest for command interpreter.
"""

import os
import sys
import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter.
    """

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("Usage: create <class_name>\n        "
             "Create a new instance of BaseModel, save it, and print the id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = ("Print the string representation of an instance\n        "
             "Usage: show BaseModel 3195da8d-2c7e-464b-a028-1f123247f74f")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Delete an instance based on class name and id.\n        "
             "Usage: destroy BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Print all string representations of instances\n        "
             "Usage: all Basemodel or all")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Update an instance attribute based on classname and id\n        "
             "Usage: update <class> <id> <attribute name> <attribute value>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing the 'show' command in HBNBCommand.
    """

    def test_show_missing_class_name(self):
        class_missing = "* class name missing *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(class_missing, output.getvalue().strip())

    def test_show_invalid_class_name(self):
        nonexistent = "* class doesn't exist *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show InvalidClass 12345"))
            self.assertEqual(nonexistent, output.getvalue().strip())

    def test_show_missing_instance_id(self):
        no_instance = "* instance id missing *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(no_instance, output.getvalue().strip())

    def test_show_nonexistent_instance(self):
        no_instance = "* no instance found *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12345"))
            self.assertEqual(no_instance, output.getvalue().strip())

	    class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing the 'destroy' command in HBNBCommand.
    """

    def test_destroy_missing_class_name(self):
        class_missing = "* class name missing *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(class_missing, output.getvalue().strip())

    def test_destroy_invalid_class_name(self):
        nonexistent = "* class doesn't exist *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy InvalidClass 12345"))
            self.assertEqual(nonexistent, output.getvalue().strip())

    def test_destroy_missing_instance_id(self):
        no_instance = "* instance id missing *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(no_instance, output.getvalue().strip())

    def test_destroy_nonexistent_instance(self):
        no_instance = "* no instance found *"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 12345"))
            self.assertEqual(no_instance, output.getvalue().strip())

class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing the 'all' command in HBNBCommand.
    """

    def test_all_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all InvalidClass"))
            self.assertEqual("* class doesn't exist *",
                             output.getvalue().strip())

    def test_all_with_valid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertTrue(isinstance(output.getvalue(), str))
class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing the 'update' command in HBNBCommand.
    """

    def test_update_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("* class name missing *", output.getvalue().strip())

    def test_update_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update InvalidClass 12345"))
            self.assertEqual("* class doesn't exist *", output.getvalue().strip())

    def test_update_missing_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual("* instance id missing *", output.getvalue().strip())

    def test_update_nonexistent_instance(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 12345"))
            self.assertEqual("* no instance found *", output.getvalue().strip())



if __name__ == '__main__':
    unittest.main()

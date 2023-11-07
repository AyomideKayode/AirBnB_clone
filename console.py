#!/usr/bin/python3

"""Console Module.
This is the entry point of our command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when empty line + ENTER"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = BaseModel()
            obj.save()
            print(obj.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance
        Usage: show BaseModel 3195da8d-2c7e-464b-a028-1f123247f74f
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id
        Usage: destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances
        Usage: all Basemodel or all
        """
        args = arg.split()
        objects = storage.all()

        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif len(args) == 1 and args[0] in ["BaseModel"]:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute based on class name and id
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attribute_name = args[2]
        attribute_value = args[3]

        if hasattr(obj, attribute_name):
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

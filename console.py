#!/usr/bin/python3

"""Console Module.
This is the entry point of our command interpreter.
"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
This module creates a command line interpreter (console) which serves as the
entry point for the AirBnB project.

Class:
    HBNBCommand: Defines commands available on the AirBnB console

Attributes:
    None

Functions:
    None
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the commands available on our AirBnB Console."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the interpreter."""
        return True

    def emptyline(self):
        pass

    do_EOF = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()

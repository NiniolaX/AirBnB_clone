#!/usr/bin/python3
import cmd
"""
This module contains the command interpreter for our AirBnB project.

Class:
    HBNBCommand: Command interpreter for AirBnB project

Attributes:
    None

Functions:
    None
"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the interpreter."""
        return True

    def emptyline(self):
        pass

    do_EOF = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()

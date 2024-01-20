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
        """Exits the console.

        Args:
            line(str): command argument(s)

        Returns:
            Bool: True to exit console
        """
        return True

    def help_quit(self):
        """Help documentation for quit command."""
        print("Quit command to exit the program.\n")

    def do_EOF(self, line):
        """Exits the console.

        Args:
            line(str): command argument(s)

        Returns:
            Bool: True to exit console
        """
        return True

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program.\n")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

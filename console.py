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
from models.base_model import BaseModel
from models import storage
import textwrap

class_list = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """This class defines the commands available on our AirBnB Console."""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of the BaseModel class

        Args:
            args(str): name of class

        Return:
            None
        """
        if args:
            if args in class_list:
                new_instance = BaseModel()
                storage.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """Help documentation for create command"""
        help_text = """
        Create command creates a new instance of a specified class.

        Usage: create <class_name>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def do_show(self, args):
        """
        Prints the str representation of an instance based on class name and
        instance id

        Args:
            args(str): class name and instance id

        Returns:
            Nothing
        """
        if args:
            cmd_args = args.split()  # split aegs to extract class name and id

            if len(cmd_args) < 2:
                print("** instance id missing **")

            else:
                instance_class_name = cmd_args[0]
                instance_id = cmd_args[1]
                if instance_class_name not in class_list:
                    print("** class doesn't exist **")
                else:
                    all_objs = storage.all()
                    for obj_key in all_objs.keys():
                        if obj_key == f"{instance_class_name}.{instance_id}":
                            obj = all_objs[obj_key]
                            print(obj)
                        else:
                            print("** no instance found **")
        else:
            print("** class name missing **")

    def help_show(self):
        """Help documentation for show command"""
        help_text = """
        Show command prints the string representation of a specified instance
        based on its class name and id.

        Usage: show <class_name> <instance_id>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

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

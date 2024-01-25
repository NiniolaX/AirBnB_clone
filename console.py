#!/usr/bin/python3
"""
This module creates a command line interpreter (console) which serves as the
entry point for the AirBnB project.

Class:
    HBNBCommand: Defines commands available on the AirBnB console

Attributes:
    class_list: List of classes

Functions:
    format_value: Casts a given string value to its correct type.
"""


import cmd
from datetime import datetime
import textwrap
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re

class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }


def format_value(string):
    """Casts a given value from string to its correct type.

    Args:
        string(str): Value to be formatted

    Return:
        formatted_val (int, float or str): Formatted value
    """
    if '.' in string and not (string.startswith('"') and string.endswith('"')):
        formatted_val = float(string)
    elif string.isdigit() or (string[0] == '-' and string[1:].isdigit()):
        formatted_val = int(string)
    else:
        # Remove double quotes
        formatted_val = ""
        for c in string:
            if c != '"':
                formatted_val = formatted_val + c
    return formatted_val


class HBNBCommand(cmd.Cmd):
    """This class defines the commands available on our AirBnB Console."""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of a specified class in class_list

        Args:
            args(str): name of class

        Return:
            None
        """
        if not args:
            print("** class name missing **")
        else:
            class_name, *rem_args = args.split()
            if class_name not in class_list:
                print("** class doesn't exist **")
            else:
                new_instance = class_list[class_name]()
                storage.save()
                print(new_instance.id)

    def help_create(self):
        """Help documentation for create command."""
        help_text = """
        Create command creates a new instance of a specified class.
        Prints the id of the new instance on success.

        Usage: create <class_name>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def do_show(self, args):
        """
        Prints the str representation of an instance based on its class name
        and instance id.

        Args:
            args(str): instance class name and id

        Returns:
            Nothing
        """
        if not args:
            print("** class name missing **")
        else:
            cmd_args = args.split()  # split args to extract class name and id
            if len(cmd_args) == 1:
                print("** instance id missing **")
            else:
                instance_class_name = cmd_args[0]
                instance_id = cmd_args[1]
                if instance_class_name not in class_list:
                    print("** class doesn't exist **")
                else:
                    # Print instance from objects in storage
                    all_objs = storage.all()
                    instance_key = f"{instance_class_name}.{instance_id}"
                    if instance_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        instance = all_objs[instance_key]
                        print(instance)

    def help_show(self):
        """Help documentation for show command."""
        help_text = """
        Show command prints the string representation of a specified instance
        based on its class name and id.

        Usage: show <class_name> <instance_id>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def do_destroy(self, args):
        """Deletes an instance based on its class name and id.

        Args:
            args(str): instance class name and id

        Returns:
            Nothing
        """
        if not args:
            print("** class name missing **")
        else:
            cmd_args = args.split()  # split args to extract class name and id
            if len(cmd_args) == 1:
                print("** instance id missing **")
            else:
                instance_class_name = cmd_args[0]
                instance_id = cmd_args[1]

                if instance_class_name not in class_list:
                    print("** class doesn't exist **")
                else:
                    all_objs = storage.all()
                    instance_key = f"{instance_class_name}.{instance_id}"
                    if instance_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        del all_objs[instance_key]
                        storage.save()

    def help_destroy(self):
        """Help documentation for destroy command."""
        help_text = """
        Destroy command deletes an instance based on its class name and id.

        Usage: destroy <class_name> <instance_id>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def do_all(self, args=None):
        """
        Prints the string representation of all instances based or not on the
        class name.

        Args:
            args(str): class name (optional)

        Returns:
            Nothing
        """
        all_instances = []
        all_objs = storage.all()
        if args:
            # Print all instances of class name in storage
            all_args = args.split()
            class_name = all_args[0]
            if class_name not in class_list:
                print("** class doesn't exist **")
            else:
                for obj_key, obj_value in all_objs.items():
                    if obj_key.startswith(class_name + '.'):
                        all_instances.append(str(obj_value))
                print(all_instances)
        else:
            # Print all instances in storage
            for obj_key, obj_value in all_objs.items():
                all_instances.append(str(obj_value))
            print(all_instances)

    def help_all(self):
        """Help documentation for all method."""
        help_text = """
        All command prints all string representation of all instances based or
        not on the class name

        Usage: all <class_name> or all
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.

        Args:
            args(str): classname, id, attribute name and attribute value

        Returns:
            Nothing
        """
        if not args:
            print("** class name missing **")
        else:
            class_name, *rem_args = args.split()

            if class_name not in class_list:
                print("** class doesn't exist **")
                return

            if not rem_args:
                print("** instance id missing **")
                return

            instance_id = rem_args[0]  # setting 2nd arg as instance id
            # Check if instance of class name provided exists
            all_instances = storage.all()
            instance_key = f"{class_name}.{instance_id}"
            if instance_key not in all_instances.keys():
                print("** no instance found **")
                return

            if len(rem_args) < 2:
                print("** attribute name missing **")
                return
            attr_name = rem_args[1]

            if len(rem_args) < 3:
                print("** value missing **")
                return
            attr_value = rem_args[2]

            # Extract instance
            instance = all_instances[instance_key]

            # Update instance
            setattr(instance, attr_name, format_value(attr_value))
            self.updated_at = datetime.now()
            storage.save()

    def help_update(self):
        """Help documentation for update command."""
        help_text = """
        Update command updates an instance based on its class name and id
        by adding or updating attribute.

        Usage: update <class_name> <instance_id> <attr_name> <attr value>
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def onecmd(self, args):
        """Executes a single command passed as a string.

        Args:
            args(str): Single command
        """
        if '.' in args:
            # Extract class_name and cmd name first
            class_name, cmd, *rem_args = re.split(r'\.|\(|\,|\)', args)
            if rem_args:
                # Extract remaining arguments from list rem_args to a string
                cmd_args = "".join(arg for arg in rem_args)
                # Add class name to beginning of arguments
                all_args = class_name + ' ' + cmd_args
            try:
                # Obtain specified command method and pass arguments to it
                getattr(self, f"do_{cmd}")(all_args)
            except AttributeError:
                # Handle error properly if command is not found
                print(f"*** Unknown syntax: {cmd}")
        else:
            # Call the superclass implementation for other commands
            return super().onecmd(args)

    def do_count(self, args):
        """Counts the number of instances of a specified class in storage.

        Args:
            args(str): Class name or null

        Return:
            Nothing
        """
        instance_count = 0
        all_instances = storage.all()
        if not args:
            instance_count = len(all_instances)
        else:
            class_name, *rem_args = args.split()
            for key in all_instances.keys():
                if key.startswith(class_name + '.'):
                    instance_count = instance_count + 1
        print(instance_count)

    def help_count(self):
        """Help documentation for count command."""
        help_text = """
        Count command prints the number of instances in storage based on class
        name or not.

        Usage: <class_name>.count()
        Returns: Nothing
        """
        formatted_help_text = textwrap.dedent(help_text)
        print(formatted_help_text)

    def emptyline(self):
        """Handles emptyline + ENTER"""
        pass

    def do_quit(self, line):
        """Exits the console.

        Args:
            args(str): command argument(s)

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
            args(str) command argument(s)

        Returns:
            Bool: True to exit console
        """
        print()
        return True

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program.\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

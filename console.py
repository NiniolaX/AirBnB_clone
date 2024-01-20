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
    prompt = "(hbnb) "

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
        if args:
            cmd_args = args.split()  # split args to extract class name and id
            if len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                instance_class_name = cmd_args[0]
                instance_id = cmd_args[1]
                if instance_class_name not in class_list:
                    print("** class doesn't exist **")
                else:
                    # Extract instance from objects in storage
                    all_objs = storage.all()
                    instance_key = f"{instance_class_name}.{instance_id}"
                    if instance_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        for obj_key in all_objs.keys():
                            if obj_key == instance_key:
                                instance = all_objs[obj_key]
                                print(instance)  # Print instance
        else:
            print("** class name missing **")

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
        if args:
            cmd_args = args.split()  # split args to extract class name and id
            if len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                instance_class_name = cmd_args[0]
                instance_id = cmd_args[1]

                if instance_class_name in class_list:
                    all_objs = storage.all()
                    instance_key = f"{instance_class_name}.{instance_id}"
                    if instance_key in all_objs.keys():
                        del all_objs[instance_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
            all_args = args.split()
            class_name = all_args[0]
            if class_name in class_list:
                # Print all instances of class_name in storage
                for obj_key, obj_value in all_objs.items():
                    if obj_key.startswith(class_name + '.'):
                        all_instances.append(str(obj_value))
                print(all_instances)
            else:
                print("** class doesn't exist **")
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

    def do_quit(self, args):
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

    do_EOF = do_quit

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program.\n")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

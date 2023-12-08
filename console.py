#!/usr/bin/python3
""" this program creates a console
Which serves as an entry point of a command interpreter
"""


# import the cmd module
import cmd
from models.base_model import BaseModel  # import the BaseModel
from datetime import datetime
from models import storage


class HBNBCommand(cmd.Cmd):
    """this classs defines the functionality of a CLI
    It inherits all the features of the Cmd class
    via this class we can run methods that acts like a native shell command
    """

    # create a list of all allowed/available classes
    class_list = {'BaseModel': BaseModel}

    # create a custom prompt
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        if not args:  # if class name is missing
            print("** class name missing **")
            return

        if args not in self.class_list:
            print("** class doesn't exist **")
            return

        # split args to extract contents
        args = args.split()
        class_name = args[0]  # extract first arg as class_name

        # create instance from the given class name
        instance = self.class_list[class_name]()
        # save it to the JSON file
        instance.save()
        # print the ID
        print(instance.id)

    def do_show(self, args):
        """prints the str representation of an instance
        this is done based on class name and id
        """
        # get class name (first arg) and id second arg, so split by space
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        # get instances from the storage variable in __init__
        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        The changes are saved into the JSON file
        e.g: $ destroy BaseModel 1234-1234-1234
        """
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        # set first arg as class name
        class_name = args[0]

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        # get all instances
        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        if instance_key not in instances:
            print("** no instance found **")
            return

        # if all true, delete the instance
        del instances[instance_key]
        # save changes to json
        storage.save()

    def do_all(self, args):
        """prints all string representation of all instances
        printing is based on  or not on the class name
        i.e whether: all BaseModel or all
        """

        args = args.split()  # split the args string into separate arguments

        class_name = None  # set default value for class_name

        if args and args[0] not in self.class_list:
            print("** class doesn't exist **")
            return

        if args:
            class_name = args[0]

        instances = storage.all()
        for instance_key in instances:
            if class_name is None or instance_key.startswith(class_name):
                print(instances[instance_key])

    def do_update(self, args):
        """updates the instances based on the classs name and id
        this is done by adding or updating attr
        changes/updates are saved into the JSON file)
        e.g $ update BaseModel 1234-1234-1234 email "aibnb@gmail.com
        """
        if not args:
            print("** class name missing **")
            return

        args = args.split()  # split the args string into separate arguments
        class_name = args[0]

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        # set second arg as instance id
        instances = storage.all()
        instance_key = args[0] + "." + args[1]

        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) == 3:
            print("** value missing **")
            return

        value = args[3].strip('"')
        instance = instances[instance_key]

        # set the new attribute for the specific instance
        setattr(instance, attr_name, value)
        instance.updated_at = datetime.now()
        instance.save()  # save to JSON file

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ quits the console when 'EOF' is triggered"""
        print()
        return True

    def emptyline(self):
        """defines what happens when an empty line is entered"""
        pass  # do nothing

    def help_quit(self):
        """Help documentation for quit command"""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """Help documentation for EOF command"""
        print('EOF command to exit the program\n')


# run the program only when it's not imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()

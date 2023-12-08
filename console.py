#!/usr/bin/python3
""" this program creates a console
Which serves as an entry point of a command interpreter
"""


# import the cmd module
import cmd
import json
import re
from models.base_model import BaseModel  # import the BaseModel
from datetime import datetime
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# create a list of all allowed/available classes
class_list = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """this classs defines the functionality of a CLI
    It inherits all the features of the Cmd class
    via this class we can run methods that acts like a native shell command
    """

    # create a custom prompt
    prompt = "(hbnb) "

    def onecmd(self, line):
        match = re.match(r'^(?P<class_name>\w+)\.all\(\)$', line)
        if match:
            class_name = match.group('class_name')
            if class_name in class_list:
                self.do_all(class_name)
            else:
                print("*** class doesn't exist **")
            return

        match = re.match(r'^(?P<class_name>\w+)\.count\(\)$', line)
        if match:
            class_name = match.group('class_name')
            if class_name in class_list:
                instances = storage.all()
                count = sum(1 for instance_key
                        in instances if
                        instance_key.startswith(
                            class_name)
                        )
                print(count)
            else:
                print("** class doesn't exist **")
            return

        match = re.match(r'^(?P<class_name>\w+)\.show\(["\']?(?P<id>[\w-]+)["\']?\)$', line)
        if match:
            class_name = match.group('class_name')
            id_ = match.group('id')
            if class_name in class_list:
                # construct the arg string
                args = class_name + " " + id_
                self.do_show(args)
            else:
                print("*** class doesn't exist **")
            return

        match = re.match(r'^(?P<class_name>\w+)\.destroy\(["\']?(?P<id>[\w-]+)["\']?\)$', line)
        if match:
            class_name = match.group('class_name')
            id_ = match.group('id')
            if class_name in class_list:
                # construct the arg string
                args = class_name + " " + id_
                self.do_destroy(args)
            else:
                print("*** class doesn't exist **")
            return

        # handle the first scenario
        match = re.search(r'(?P<class_name>\w+)\.update\((?P<id>\w+), (?P<attr_name>\w+), (?P<attr_value>.*)\)', line)
        if match:
            class_name = match.group('class_name')
            id_ = match.group('id')
            attr_name = match.group('attr_name')
            attr_value = match.group('attr_value').strip('"')
            args = class_name + ' ' + id_ + ' ' + attr_name + ' ' + attr_value
            if class_name in class_list:
                self.do_update(args)
            else:
                print('** class doesn\'t exist **')
            return
        # handle the second scenario
        match = re.search(r'(?P<class_name>\w+)\.update\((?P<id>\w+), (?P<attr_dict>.*)\)', line)
        
        if match:
            class_name = match.group('class_name')
            id_ = match.group('id')
            attr_dict = json.loads(match.group('attr_dict').strip('"'))
            args = class_name + ' ' + id_ + ' ' + attr_dict
            if class_name in class_list:
                self.do_update(args)
            else:
                print('** class doesn\'t exist **')
            return

        return super().onecmd(line)

    def do_create(self, args):
        """creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        if not args:  # if class name is missing
            print("** class name missing **")
            return

        if args not in class_list:
            print("** class doesn't exist **")
            return

        # split args to extract contents
        args = args.split()
        class_name = args[0]  # extract first arg as class_name

        # create instance from the given class name
        instance = class_list[class_name]()
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
        if class_name not in class_list:
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

        if class_name not in class_list:
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

        if args and args[0] not in class_list:
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

        if class_name not in class_list:
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

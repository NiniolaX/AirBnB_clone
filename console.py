#!/usr/bin/python3
"""this program creates a console
Which serves as an entry point of a command interpreter
"""


from datetime import datetime
import json
import re

import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


"""create a dictionary mapping class names to class objects"""
class_list = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


def normalize_value(str_v):
    """function to normalize values"""
    # check if the value is an integer
    if str_v.isdigit() or (str_v[0] == '-' and str_v[1:].isdigit()):
        return int(str_v)
    # if its just a regular string but has double quotes
    elif str_v.startswith('"') and not str_v.endswith('"'):
        return str_v.stri('"')

    # check if the value is a float
    try:
        return float(str_v)
    except (ValueError, Exception):
        # return as it is if neither int or float
        return str_v.strip('"')

    # check if the attr is enclosed in double quotes
    if str_v.startswith('"') and str_v.endswith('"'):
        return str_v[1:-1]  # Remove the double quotes
    else:
        return str_v.strip('"')  # remove the double uotes if found


class HBNBCommand(cmd.Cmd):
    """this classs defines the functionality of a cli
    It inherits all the features of the _cmd class
    via this class we can run methods that acts like a native shell command
    """

    # create a custom prompt
    prompt = "(hbnb) "

    def onecmd(self, line):
        """this method handles default behaviours of commands"""
        match = re.match(r'^(?P<class_name>\w*)\.all\(\)$', line)
        if match:
            class_name = match.group('class_name')
            if not class_name:
                print("** class name missing **")
                return

            if class_name in class_list:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
            return

        match = re.match(r'^(?P<class_name>\w*)\.count\(\)$', line)
        if match:
            class_name = match.group('class_name')
            if not class_name:
                print("** class name missing **")
                return
            if class_name not in class_list:
                print("** class doesn't exist **")
                return

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

        match = re.match(
            r'^(?P<cls_n>\w*)\.show\(["\']?(?P<id>[\w-]*)["\']?\)$',
            line)
        if match:
            class_name = match.group('cls_n')
            if not class_name:
                print("** class name missing **")
                return
            if class_name not in class_list:
                print("** class doesn't exist **")
                return

            id_ = match.group('id')
            if not id_:
                print("** instance id missing **")
                return
            if class_name in class_list:
                # construct the arg string
                args = f"{class_name} {id_}"
                self.do_show(args)
            else:
                print("** class doesn't exist **")
            return

        match = re.match(
            r'^(?P<cls_n>\w*)\.destroy\(["\']?(?P<id>[\w-]*)["\']?\)$',
            line)
        if match:
            class_name = match.group('cls_n')
            if not class_name:
                print("** class name missing **")
                return
            if class_name not in class_list:
                print("** class doesn't exist **")
                return

            id_ = match.group('id')
            if not id_:
                print("** instance id missing **")
                return
            if class_name in class_list:
                # construct the arg string
                args = f"{class_name} {id_}"
                self.do_destroy(args)
            else:
                print("** class doesn't exist **")
            return

        # if the command starts with a class name and dot 'Class.update'
        if '.' in line and line.split('.')[1].startswith('update'):
            # Extract the class name and the rest of the command
            class_name, r_cmd = line.split('.', 1)

            # check for classname
            if not class_name:
                print("** class name missing **")
                return
            if class_name not in class_list:
                print("** class doesn't exist **")
                return

            # Remove the 'update' part and the parentheses
            r_cmd = r_cmd.replace('update', '')\
                .replace('(', '').replace(')', '')

            if len(r_cmd) == 0:
                print("** instance id missing **")
                return

            # Split the command into parts
            parts = [part.strip() for part in r_cmd.split(',', 1)]

            # get the id
            id_ = parts[0].strip('"')

            if len(parts) == 2 and parts[1].startswith('{')\
                    and parts[1].endswith('}'):
                try:
                    attr_dict = eval(parts[1].replace("'", '"'))
                except Exception as e:
                    print(str(e))
                    return
                # combine the class,id andn dict into one str
                args = '{} {} {}'.format(
                        class_name, id_, str(attr_dict).replace('\'', '\"'))
                self.do_update(args)
                return
            else:
                # if not dict assume reg values
                if len(parts) == 1:
                    print("** attribute name missing **")
                    return

                # Check if parts[1] has only one element
                if len(parts[1].split(',')) == 1:
                    print("** value missing **")
                    return

                try:
                    attr_name, attr_value = \
                            [part.strip() for part in parts[1].split(',', 1)]
                except Exception as e:
                    print(str(e))
                    return
                # check missing attribute
                if not attr_value:
                    print("** value missing **")
                    return
                # combine class, name, id, attr, val to one str
                args = f"{class_name} {id_} {attr_name} {attr_value}"

            # call method on args
            self.do_update(args)
            return
        return super().onecmd(line)

    def do_create(self, args):
        """creates a new instance of base_model
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

        # get instances from the storage variable in
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
        """

        args = args.split()  # split the args string into separate arguments

        class_name = None  # set default value for class_name

        if args and args[0] not in class_list:
            print("** class doesn't exist **")
            return

        if args:
            class_name = args[0]

        instances = storage.all()
        instance_list = []
        for instance_key in instances:
            if class_name is None or instance_key.startswith(class_name):
                instance_list.append(str(instances[instance_key]))
        print(instance_list)

    def do_update(self, args):
        """updates the instances based on the classs name and id
        this is done by adding or updating attr
        changes/updates are saved into the JSON file)
        """

        if not args:
            print("** class name missing **")
            return

        class_name, *rest_args = args.split()  # split the args into sep arg

        if class_name not in class_list:
            print("** class doesn't exist **")
            return

        if not rest_args:
            print("** instance id missing **")
            return

        # set second arg as instance id
        instances = storage.all()
        instance_key = class_name + "." + rest_args[0]

        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(rest_args) == 1:
            print("** attribute name missing **")
            return

        instance = instances[instance_key]

        if rest_args[1].startswith('{') and rest_args[-1].endswith('}'):
            try:
                # convert single quotes to double quotes
                json_str = ' '.join(rest_args[1:])
                value_dict = json.loads(json_str)

                for key, value in value_dict.items():
                    setattr(instance, key, value)
            except (json.JSONDecodeError, Exception) as e:
                print("json.JSONDecodeError ", str(e))
                pass
        else:
            if len(rest_args) == 2:
                print("** value missing **")
                return

            attr_name = rest_args[1].strip('"')
            value = ' '.join(rest_args[2:]).strip('"')  # Join val wt spaces
            # set the new attr for the specific instance
            setattr(instance, attr_name, normalize_value(value))

        instance.updated_at = datetime.now()
        instance.save()  # save to JSON file

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """quits the console when eof is triggered"""
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

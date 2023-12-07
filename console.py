#!/usr/bin/python3
""" this program creates a console
Which serves as an entry point of a command interpreter
"""


# import the cmd module
import cmd


class HBNBCommand(cmd.Cmd):
    """this classs defines the functionality of a CLI
    It inherits all the features of the Cmd class
    via this class we can run methods that acts like a native shell command
    """

    # create a custom prompt
    prompt = "(hbnb) "

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

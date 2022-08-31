#!/usr/bin/python3
"""Module containing the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models.user import User

avaliable_classes = {'BaseModel': BaseModel, 'User': User}


class HBNBCommand(cmd.Cmd):
    """This class represents the command interpreter
    of this project."""

    prompt = '(hbnb) '

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance.
        """
        args = arg.split()
        if not check_classname(args):
            return

        new_obj = avaliable_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not check_classname(args, id=True):
            return


def check_classname(args, id=False):
    """Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in avaliable_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and id:
        print("** instance id missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

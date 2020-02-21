#!/usr/bin/python3
"""
This module contain the class HBNBCommand
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """This class of a Simple command processor"""

    prompt = "(hbnb)"
    myclasses = {"BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"}

    def do_create(self, args):
        """This func creates new instance of the class BaseModel,
        saves it (to JSON file) and prints the id """

        if not args:
            print("** class name missing **")
            return
        elif args not in self.myclasses:
            print("** class doesn't exist **")
        else:
            args = args.split()
            token = eval(args[0])()
            token.save()
            print(token.id)

    def do_show(self, args):
        """ This func Prints the string representation of an instance based
        on the class name and id"""

        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing ** ")
        else:
            data = storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                print(data[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """ This func Deletes an instance based on the class name
        and id (save the change into the JSON file)."""

        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        data = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in data.keys():
            print("** no instance found **")
            return
        del data[key]
        storage.save()

    def do_all(self, args):
        """This func Prints all string representation of all instances
        based or not on the class name.  """

        data = storage.all()
        if len(args) == 0:
            for my_inst_key, my_inst_object in data.items():
                print(my_inst_object)
        else:
            args = args.split()
            if args[0] not in self.myclasses:
                print("** class doesn't exist **")
            else:
                mylist = []
                for my_inst_object in data.values():
                    if my_inst_object.__class__.__name__ == args[0]:
                        mylist.append(str(my_inst_object))
                print(mylist)

    def do_update(self, args):
        """
        This func Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """

        args = args.split()
        data = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.myclasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in data:
            try:
                ob_value = data[key]
                setattr(ob_value, args[2], args[3])
            except:
                print("** no instance found **")

    def do_quit(self, args):
        """This func exit the program"""

        return True

    def do_EOF(self, line):
        """This func exit the program for EOF signal """
        return True

    def emptyline(self):
        """This func shouldn t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

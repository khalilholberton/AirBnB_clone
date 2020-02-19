#!/usr/bin/python3
"""
this module contain the class HBNBCommand
"""
import cmd
import models
import json
from models import storage
from models.base_model import BaseModel
from shlex import split



class HBNBCommand(cmd.Cmd):
    """Simple command processor"""

    prompt = "(hbnb)"
    myclasses = {"BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"}

    def do_create(self, args):
        """creates new instance of the class BaseModel, saves it (to JSON file)
        and prints the id """

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
        """do_show"""

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
        """do_destroy"""

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



    def do_quit(self, args):
        """exit the program"""

        return True

    def do_EOF(self, line):
        """exit the program for EOF signal """
        return True

    def emptyline(self):
        """shouldn t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

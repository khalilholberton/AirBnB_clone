#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""

    prompt = "(hbnb)"

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

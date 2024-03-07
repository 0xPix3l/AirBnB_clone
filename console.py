#!/usr/bin/env python3
""" This module contains the HBNBCommand class """


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ This class represents a command interpreter """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """ Ctrl+d exits from the interpreter\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # non interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()

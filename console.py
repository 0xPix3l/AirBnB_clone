#!/usr/bin/env python3
""" This module contains the HBNBCommand class """

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This class represents a command interpreter. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, line):
        """ Ctrl+d exits from the interpreter.\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """ Creates a new instance of class name, saves it (to the JSON file),
        and prints the ID\n"""
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                # Use FileStorage instance to add new instance
                storage.new(new_instance)
                storage.save()  # Save the changes to file
                print(new_instance.id)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # non-interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()

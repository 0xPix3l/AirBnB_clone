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

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
    name and id\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = '{}.{}'.format(class_name, obj_id)
        obj_dict = storage.all().get(obj_key)

        if not obj_dict:
            print("** no instance found **")
            return

        # Create an instance based on the class name and print it
        obj_instance = BaseModel(**obj_dict)
        print(obj_instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = '{}.{}'.format(class_name, obj_id)
        obj_dict = storage.all().get(obj_key)

        if not obj_dict:
            print("** no instance found **")
            return

        # Remove the instance from __objects and save the changes to file
        del storage.all()[obj_key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name\n"""
        args = line.split()
        instances = storage.all()
        output = []

        if not args or args[0] not in ["BaseModel"]:
            for value in instances.values():
                output.append(str(BaseModel(**value)))
        else:
            class_name = args[0]
            for key, value in instances.items():
                if key.startswith(class_name):
                    output.append(str(BaseModel(**value)))

        print(output)

    def do_update(self, line):
        """Updates an instance based on the class name and id
by adding or updating attribute (save the change into the JSON file).
    Usage: update <class name> <id> <attribute name> "<attribute value>\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = '{}.{}'.format(class_name, obj_id)
        obj_dict = storage.all().get(obj_key)

        if not obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        obj_instance = BaseModel(**obj_dict)

        # Check if the attribute already exists in the dictionary
        if hasattr(obj_instance, attr_name):
            # Check if the attribute already exists in the dictionary
            setattr(obj_instance, attr_name, attr_value)
        else:
            # If the attribute doesn't exist, add it to the dictionary
            obj_dict[attr_name] = attr_value

        storage.save()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # non-interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()

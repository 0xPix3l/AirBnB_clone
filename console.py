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
    classname_list = ["BaseModel", "City", "State",
                      "User", "Place", "Review", "Amenity"]

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
            return
        elif (line not in self.classname_list):
            print("** class doesn't exist **")
            return
        else:
            inst = eval(line + '()')
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif (args[0] not in self.classname_list):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                print(obj)

                # obj_id = args[1]
                # class_name = args[0]
                # obj_key = '{}.{}'.format(class_name, obj_id)
                # obj_dict = storage.all().get(obj_key)
                # obj_instance = BaseModel(**obj_dict)
                # print(obj_instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)\n"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif (args[0] not in self.classname_list):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name\n"""
        args = line.split()
        output = []
        if len(args) == 0:
            for value in storage.all().values():
                output.append(value.__str__())
            print(output)
        elif (args[0] not in self.classname_list):
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args[0] in key:
                    output.append(storage.all()[key].__str__())
                else:
                    return
                print(output)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classname_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj_dict = storage.all().get(key)
        if not obj_dict:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        # Update the attribute in the dictionary
        obj_dict[attr_name] = attr_value
        # Save the changes to file
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

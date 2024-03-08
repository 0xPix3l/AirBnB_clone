#!/usr/bin/env bash
""" This module contains the FileStorage class """


import json
from os.path import exists


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
         returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        type(self).__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        file = type(self).__file_path

        json_str = json.dumps(self.all())

        with open(file, "w+", encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        file = type(self).__file_path
        if exists(file):
            with open(file, encoding='utf-8') as f:
                json_str = f.read()
                print('\n\n{}\n\n'.format(json_str))
                type(self).__objects = json.loads(json_str)

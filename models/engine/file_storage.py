#!/usr/bin/env bash
""" This module contains the FileStorage class """

import json
from os.path import exists
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

        # Check the class type and handle serialization
        if type(obj).__name__ in ['User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            type(self).__objects[key] = obj.to_dict()
        else:
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
                # Load JSON data into objects
                loaded_data = json.loads(json_str)

                # Dictionary to map class names to corresponding class types
                class_mapping = {
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                }

                # Iterate over the loaded data
                for key, value in loaded_data.items():
                    # Split the key to get class name and instance id
                    class_name, obj_id = key.split()

                    # Check if the class is in the class_mapping dictionary
                    if class_name in class_mapping:
                        # Create a new instance of the corresponding class
                        new_instance = class_mapping[class_name](**value)
                    else:
                        # If class not found, default to creating a BaseModel instance
                        new_instance = BaseModel(**value)

                    # Update __objects dictionary
                    type(self).__objects[key] = new_instance

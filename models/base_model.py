#!/usr/bin/env python3

"""
This file is the BaseModel for all of
the future classes in the project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """ Base class for all classses. """

    def __init__(self):
        """ Attributes:
        id
        created_at
        updated_at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns string representation of the following attributes:
        Class Name
        id of the instance
        dict """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Updates the creation time of the
        attribute with the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance. """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict

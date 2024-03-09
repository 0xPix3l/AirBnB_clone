#!/usr/bin/env bash
""" This module contains the 'Amenity' class """


from models import BaseModel


class Amenity(BaseModel):
    """ This class inherits from the BaseModel class """
    name = ''

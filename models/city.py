#!/usr/bin/env bash
""" This module contains the 'City' class """


from models.base_model import BaseModel


class City(BaseModel):
    """ This class inherits from the BaseModel class """
    state_id = ''
    name = ''

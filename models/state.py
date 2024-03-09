#!/usr/bin/env bash
""" This module contains the 'State' class """


from models.base_model import BaseModel


class State(BaseModel):
    """ This class inherits from the BaseModel class """
    name = ''

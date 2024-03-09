#!/usr/bin/python3
""" User. """
from . base_model import BaseModel


class User(BaseModel):
    """ class User inherits from BaseModel """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
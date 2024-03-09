#!/usr/bin/env bash
""" This module contains the 'Review' class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ This class inherits from the BaseModel class """
    place_id = ''
    user_id = ''
    text = ''

#!/usr/bin/env python3

"""
This file is the BaseModel for all of 
the future classes in the project.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base class for all classses. """

    def __init__(self, *args, **kwargs):

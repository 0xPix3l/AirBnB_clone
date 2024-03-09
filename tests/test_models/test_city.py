#!/usr/bin/env bash
""" This module contains the 'TestCity' class """


import unittest
from models.city import City
from models.base_model import BaseModel
from models.state import State


class TestCity(unittest.TestCase):
    """ This class tests the City class """

    def setUp(self):
        """ Called before executing the test method """
        self.my_state = State()
        self.my_city = City()

    def test_attributes(self):
        """ Tests city attributes """
        self.my_city.state_id = self.my_state.id
        self.my_city.name = "Giza"

        self.assertEqual(self.my_city.state_id, self.my_state.id)
        self.assertEqual(self.my_city.name, "Giza")

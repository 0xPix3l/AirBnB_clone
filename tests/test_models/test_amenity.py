#!/usr/bin/env bash
""" This module contains the 'TestAmenity' class """


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ This class tests the Amenity class """

    def setUp(self):
        """ Called before executing the test method """
        self.my_amenity = Amenity()

    def test_attributes(self):
        """ Tests Amenity attributes """
        self.my_amenity.name = "Wifi"

        self.assertEqual(self.my_amenity.name, "Wifi")

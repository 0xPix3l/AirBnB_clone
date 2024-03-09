#!/usr/bin/env bash
""" This module contains the 'TestPlace' class """


import unittest
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """ This class tests the Place class """

    def setUp(self):
        """ Called before executing the test method """
        self.my_place = Place()
        self.my_city = City()
        self.my_user = User()
        self.my_amenity = Amenity()

    def test_attribue(self):
        """ Tests Place attributes """
        self.my_place.city_id = self.my_city.id
        self.my_place.user_id = self.my_user.id
        self.my_place.name = "MLS hotel"
        self.my_place.description = "A neat and calm hotel"
        self.my_place.number_rooms = 50
        self.my_place.number_bathrooms = 5
        self.my_place.max_guest = 100
        self.my_place.price_by_night = 99
        self.my_place.latitude = 122.3328
        self.my_place.longtitude = 47.6061
        self.my_place.amenity_ids = [self.my_amenity]

        self.assertEqual(self.my_place.city_id, self.my_city.id)
        self.assertEqual(self.my_place.user_id, self.my_user.id)
        self.assertEqual(self.my_place.name, "MLS hotel")
        self.assertEqual(self.my_place.description, "A neat and calm hotel")
        self.assertEqual(self.my_place.number_rooms, 50)
        self.assertEqual(self.my_place.number_bathrooms, 5)
        self.assertEqual(self.my_place.max_guest, 100)
        self.assertEqual(self.my_place.price_by_night, 99)
        self.assertEqual(self.my_place.latitude, 122.3328)
        self.assertEqual(self.my_place.longtitude, 47.6061)
        self.assertEqual(self.my_place.amenity_ids, [self.my_amenity])

#!/usr/bin/env bash
""" This module contains the 'TestReview' class """


import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """ This class tests the Review class """

    def setUp(self):
        """ Called before executing the test method """
        self.my_review = Review()
        self.my_place = Place()
        self.my_user = User()

    def test_attributes(self):
        """ Tests Review attributes """
        self.my_review.place_id = self.my_place.id
        self.my_review.user_id = self.my_user.id
        self.my_review.text = "any text"

        self.assertEqual(self.my_review.place_id, self.my_place.id)
        self.assertEqual(self.my_review.user_id, self.my_user.id)
        self.assertEqual(self.my_review.text, "any text")

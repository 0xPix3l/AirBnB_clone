#!/usr/bin/python3


"""Unittest for User."""


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ This class tests the User class """ 
    def setUp(self):
        """ Called before executing the test method """
        self.my_user = User()
        
    def test_attributes(self):
        """ Tests User attributes """
        self.my_user.email = "au@gmail.com"
        self.my_user.password = "12345678"
        self.my_user.first_name = "John"
        self.my_user.last_name = "Smith"

        self.assertEqual(self.my_user.email, "au@gmail.com")
        self.assertEqual(self.my_user.password, "12345678")
        self.assertEqual(self.my_user.first_name, "John")
        self.assertEqual(self.my_user.last_name, "Smith")

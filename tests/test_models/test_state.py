#!/usr/bin/env bash
""" This module contains the TestState class """


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ This class tests the State class """

    def setUp(self):
        """ called before executing the test method """
        self.my_state = State()

    def test_attribute(self):
        """ Tests the name attribute """
        self.my_state.name = "state"
        self.assertEqual(self.my_state.name, "state")

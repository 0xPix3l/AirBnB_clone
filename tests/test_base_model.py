""" Testing BaseModel. """
from models.base_model import BaseModel
import unittest
import uuid


class testBaseModel(unittest.TestCase):
    """ Tests the main model. """

    def test_attributes(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["My First Model", 89])


if __name__ == "__main__":
    unittest.main()

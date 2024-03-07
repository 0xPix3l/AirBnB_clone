""" Testing BaseModel. """
from models.base_model import BaseModel
from datetime import datetime

import unittest
import uuid


class testBaseModel(unittest.TestCase):
    """ Tests the main model. """

    def setUp(self):
        """ called before executing the test method """
        self.my_model = BaseModel()

    def test_attributes(self):
        self.my_model.name = "My First Model"
        self.my_model.number = 89
        self.assertEqual([self.my_model.name, self.my_model.number],
                         ["My First Model", 89])

        # Testing re-creating an instance with the dictionary representation
        dct = self.my_model.to_dict()
        self.my_model_2 = BaseModel(**dct)
        self.assertEqual(self.my_model_2.id, self.my_model.id)
        del dct['__class__']

        self.assertIsInstance(self.my_model_2.created_at, datetime)
        self.assertIsInstance(self.my_model_2.updated_at, datetime)
        self.assertNotEqual(self.my_model, self.my_model_2)

if __name__ == "__main__":
    unittest.main()

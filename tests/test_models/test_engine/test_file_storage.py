""" Testing FileStorage """


import unittest
from models.base_model import BaseModel
from models import storage
import json
from os.path import exists


class TestFileStorage(unittest.TestCase):
    """This class testing the FileStorage class """

    def setUp(self):
        """ called before executing the test method """
        self.model_1 = BaseModel()
        self.model_2 = BaseModel()
        self.dct = storage.all()
        self.key = '{}.{}'.format(type(self.model_1).__name__, self.model_1.id)
        self.json_file = 'file.json'
        storage.save()

    def test_all(self):
        """ Testing the all method """
        self.models_list = [self.model_1, self.model_2]

        for i, k in enumerate(self.dct.keys()):
            if i < len(self.models_list):
                obj = self.models_list[i]

                if k == '{}.{}'.format(type(obj).__name__, obj.id) and\
                   i <= len(models_list):
                    self.assertEqual(obj.to_dict(), self.dct[k])

    def test_new(self):
        """ Testing the new method """
        self.assertEqual(self.dct[self.key], self.model_1.to_dict())

    def test_save(self):
        """ Testing the save method """
        self.model_1.name = "My_First_Model"
        self.model_1.my_number = 100
        self.model_1.save()

        with open(self.json_file, encoding='utf-8') as f:
            json_str = f.read()

        dct = json.loads(json_str)
        self.assertEqual(self.dct[self.key], self.model_1.to_dict())

    def test_reload(self):
        """ Testing the reload method """
        if exists(self.json_file):
            with open(self.json_file, encoding='utf-8') as f:
                json_str = f.read()
            new_dct = json.loads(json_str)

        self.assertEqual(self.dct, new_dct)
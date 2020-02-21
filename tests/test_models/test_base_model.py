#!/usr/bin/python3
'''test'''
import unittest
import os
from models.base_model import BaseModel
import datetime
from models import *


class TestBaseModel(unittest.TestCase):
    '''Test for BaseModel class '''
    def setUp(self):
        '''set'''
        self.testbase = BaseModel(1)

    def test(self):
        '''test '''
        basemodel = BaseModel(1)
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "1"))

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        t = self.testbase.updated_at
        self.testbase.save()
        testbase_save = self.testbase.updated_at
        self.assertFalse(t == testbase_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        basemodel = BaseModel(name="amine")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

    def test_dict(self):
        '''test right forme if dict'''
        tes = BaseModel()
        form = tes.to_dict()
        self.assertTrue(hasattr(form, '__class__'))
        self.assertEqual(type(form), dict)
        self.assertEqual(type(form['created_at']), str)
        self.assertEqual(type(form['updated_at']), str)

    def test___str___(self):
        '''test str'''
        self.assertEqual(str(self.testbase),
                         "[BaseModel] ({}) {}".
                         format(self.testbase.id, self.testbase.__dict__))


if __name__ == '__main__':
    '''__name__'''
    unittest.main()

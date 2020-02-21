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

    def testto_dict(self):
        '''test right forme if dict'''
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))
        self.assertTrue(hasattr(inst, "__class__"))

    def test_str(self):
        """
        Test the return of str
        """
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".
                         format(self.base.id, self.base.__dict__))


if __name__ == '__main__':
    '''__name__'''
    unittest.main()

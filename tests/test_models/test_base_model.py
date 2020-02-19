#!/usr/bin/python3
'''test'''
import unittest
import os
from models import *
from models.base_model import BaseModel
import datetime


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

if __name__ == '__main__':
    '''__name__'''
    unittest.main()

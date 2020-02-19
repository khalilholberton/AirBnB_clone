#!/usr/bin/python3
'''test'''
import unittest
import os
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    '''Test for City s '''
    def setUp(self):
        '''set'''
        self.Cityy = City(1)

    def test(self):
        '''test '''
        Cityy = City(1)
        self.assertEqual(hasattr(Cityy, "1"))
        self.assertEqual(type(Cityy).__name__, "City")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Cityy = self.Cityy.updated_at
        self.Cityy.save()
        Cityy_save = self.Cityy.updated_at
        self.assertFalse(Cityy == Cityy_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Cityy = City(name="amine")
        self.assertEqual(type(Cityy).__name__, "City")
        self.assertFalse(hasattr(Cityy, "id"))
        self.assertFalse(hasattr(Cityy, "created_at"))
        self.assertTrue(hasattr(Cityy, "name"))
        self.assertFalse(hasattr(Cityy, "updated_at"))
        self.assertTrue(hasattr(Cityy, "__class__"))

if __name__ == '__main__':
    '''no interractive mode'''
    unittest.main()

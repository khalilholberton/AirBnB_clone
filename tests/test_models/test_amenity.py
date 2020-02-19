#!/usr/bin/python3
'''test'''
import unittest
import os
from models import *
import datetime


class TestAmenity(unittest.TestCase):
    '''Test for Amenit s '''
    def setUp(self):
        '''set'''
        self.Amnity = Amenity(1)

    def test(self):
        '''test '''
        Amnity = Amenity(1)
        self.assertEqual(hasattr(Amnity, "1"))
        self.assertEqual(type(Amnity).__name__, "Amenity")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Amnity = self.Amnity.updated_at
        self.Ammnity.save()
        Amnity_save = self.Amnity.updated_at
        self.assertFalse(Amnity == Amnity_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Amnity = Amenity(name="amine")
        self.assertEqual(type(Amnity).__name__, "Amenity")
        self.assertFalse(hasattr(Amnity, "id"))
        self.assertFalse(hasattr(Amnity, "created_at"))
        self.assertTrue(hasattr(Amnity, "name"))
        self.assertFalse(hasattr(Amnity, "updated_at"))
        self.assertTrue(hasattr(Amnity, "__class__"))

if __name__ == '__main__':
    '''__name__'''
    unittest.main()

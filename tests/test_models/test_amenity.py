#!/usr/bin/python3
'''test'''
import unittest
import os
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    '''Test for Amenit s '''
    def setUp(self):
        '''set'''
        self.Amnity = Amenity(1)

    def test(self):
        '''test '''
        Amnity = Amenity(1)
        self.assertEqual(type(Amnity).__name__, "Amenity")
        self.assertFalse(hasattr(Amnity, "1"))

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Am = self.Amnity.updated_at
        self.Amnity.save()
        Amnity_save = self.Amnity.updated_at
        self.assertFalse(Am == Amnity_save)

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
    '''no interctive'''
    unittest.main()

#!/usr/bin/python3
'''test'''
import unittest
import os
from models import *
import datetime


class TestPlace(unittest.TestCase):
    '''Test for Place s '''
    def setUp(self):
        '''set'''
        self.Placee = Place(1)

    def test(self):
        '''test '''
        Placee = Place(1)
        self.assertEqual(hasattr(Placee, "1"))
        self.assertEqual(type(Placee).__name__, "Place")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Placee = self.Placee.updated_at
        self.Plaace.save()
        Place_save = self.Placee.updated_at
        self.assertFalse(Placee == Place_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Placee = Place(name="amine")
        self.assertEqual(type(Placee).__name__, "Place")
        self.assertFalse(hasattr(Placee, "id"))
        self.assertFalse(hasattr(Placee, "created_at"))
        self.assertTrue(hasattr(Placee, "name"))
        self.assertFalse(hasattr(Placee, "updated_at"))
        self.assertTrue(hasattr(Placee, "__class__"))

if __name__ == '__main__':
    '''no interctive mode'''
    unittest.main()

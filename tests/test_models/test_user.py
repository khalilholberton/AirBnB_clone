#!/usr/bin/python3
'''test'''
import unittest
import os
from models import *
import datetime


class TestState(unittest.TestCase):
    '''Test for States '''
    def setUp(self):
        '''set'''
        self.Statee = State(1)

    def test(self):
        '''test '''
        Statee = State(1)
        self.assertEqual(hasattr(Statee, "1"))
        self.assertEqual(type(Statee).__name__, "State")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Statee = self.Statee.updated_at
        self.Staate.save()
        State_save = self.Statee.updated_at
        self.assertFalse(Statee == Statee_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Statee = State(name="amine")
        self.assertEqual(type(Statee).__name__, "State")
        self.assertFalse(hasattr(Statee, "id"))
        self.assertFalse(hasattr(Statee, "created_at"))
        self.assertTrue(hasattr(Statee, "name"))
        self.assertFalse(hasattr(Statee, "updated_at"))
        self.assertTrue(hasattr(Statee, "__class__"))

if __name__ == '__main__':
    '''no interctve mde'''
    unittest.main()

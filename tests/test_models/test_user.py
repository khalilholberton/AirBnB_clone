#!/usr/bin/python3
'''test'''
import unittest
import os
from models.User import User
import datetime


class TestUser(unittest.TestCase):
    '''Test for User '''
    def setUp(self):
        '''set'''
        self.Userr = User(1)

    def test(self):
        '''test '''
        Userr = User(1)
        self.assertEqual(hasattr(Userr, "1"))
        self.assertEqual(type(Userr).__name__, "User")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Userr = self.User.updated_at
        self.Useer.save()
        User_save = self.User.updated_at
        self.assertFalse(Userr == User_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Userr = User(name="amine")
        self.assertEqual(type(Userr).__name__, "User")
        self.assertFalse(hasattr(Userr, "id"))
        self.assertFalse(hasattr(Userr, "created_at"))
        self.assertTrue(hasattr(Userr, "name"))
        self.assertFalse(hasattr(Userr, "updated_at"))
        self.assertTrue(hasattr(Userr, "__class__"))

if __name__ == '__main__':
    '''no interctve mde'''
    unittest.main()

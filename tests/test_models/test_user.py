#!/usr/bin/python3
'''test'''
import unittest
import os
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    '''Test for User '''
    def setUp(self):
        '''set'''
        self.Userr = User(1)

    def test(self):
        '''test '''
        Userr = User(1)
        self.assertEqual(type(Userr).__name__, "User")
        self.assertFalse(hasattr(Userr, "1"))

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        u = self.Userr.updated_at
        self.Userr.save()
        User_save = self.Userr.updated_at
        self.assertFalse(u == User_save)

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

    def test_pass_name(self):
        """test user"""
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)


if __name__ == '__main__':
    '''no interctve mde'''
    unittest.main()

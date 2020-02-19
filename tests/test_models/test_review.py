#!/usr/bin/python3
'''test'''
import unittest
import os
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    '''Test for Review s '''
    def setUp(self):
        '''set'''
        self.Revieww = Review(1)

    def test(self):
        '''test '''
        Revieww = Review(1)
        self.assertEqual(type(Revieww).__name__, "Review")
        self.assertFalse(hasattr(Revieww, "1"))

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        r = self.Revieww.updated_at
        self.Revieww.save()
        Review_save = self.Revieww.updated_at
        self.assertFalse(r == Review_save)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        Revieww = Review(name="amine")
        self.assertEqual(type(Revieww).__name__, "Review")
        self.assertFalse(hasattr(Revieww, "id"))
        self.assertFalse(hasattr(Revieww, "created_at"))
        self.assertTrue(hasattr(Revieww, "name"))
        self.assertFalse(hasattr(Revieww, "updated_at"))
        self.assertTrue(hasattr(Revieww, "__class__"))

if __name__ == '__main__':
    '''no interctve mdoe'''
    unittest.main()

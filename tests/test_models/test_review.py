#!/usr/bin/python3
'''test'''
import unittest
import os
from models.Review import Review
import datetime


class TestReview(unittest.TestCase):
    '''Test for Review s '''
    def setUp(self):
        '''set'''
        self.Revieww = Review(1)

    def test(self):
        '''test '''
        Revieww = Review(1)
        self.assertEqual(hasattr(Revieww, "1"))
        self.assertEqual(type(Review).__name__, "Review")

    def type(self):
        '''type'''

    def test_save(self):
        '''test save'''
        Revieww = self.Revieww.updated_at
        self.Reeview.save()
        Review_save = self.Revieww.updated_at
        self.assertFalse(Revieww == Review_save)

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

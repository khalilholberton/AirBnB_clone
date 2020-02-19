#!/usr/bin/python3
'''test console'''
from unittest.mock import create_autospec
from console import HBNBCommand
import sys
import unittest


class Test_Console(unittest.TestCase):
    '''class to test'''
    def create(self, server=None):
        '''freate console'''
        return(HBNBCommand(stdin=self.mock_stdin,
                           stdout=self.mock_stdout))

    def setUp(self):
        '''setup'''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_ex(self):
        ''' test quit'''
        exitt = self.create()
        self.assertTrue(exitt.onecmd("qui"))

    def test_end_of_file(self):
        '''test end of file'''
        of = self.create()
        self.assertTrue(of.onecmd("EOF"))

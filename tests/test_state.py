#!/usr/bin/python3

"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        """ Create an object to test """
        self.state = State()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        """ Test the creation of the object's attributes """
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, '')
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    """ Run the test """
    unittest.main()


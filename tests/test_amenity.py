#!/usr/bin/python3

"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.amenity import Amenity

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """ Create a new object for the Amenity class """
        self.amenity = Amenity()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        """ Test the creation of attributes of the Amenity class """
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, '')
        self.assertEqual(mock_stdout.getvalue(), '')
        
if __name__ == '__main__':
    """ Run the test """
    unittest.main()
        
        
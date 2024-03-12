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
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """ Create a new object for the city class """
        self.city = City()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        """ Test the initialization of the attributes of the City class """
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(mock_stdout.getvalue(), '')
        
if __name__ == '__main__':
    """ Run the test """
    unittest.main()




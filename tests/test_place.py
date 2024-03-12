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
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        """ Create a new object for the place class """
        self.place = Place()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        """ Test the creation of the place attributes """
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    """ Run the test """
    unittest.main()


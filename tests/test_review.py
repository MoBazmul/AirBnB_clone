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
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        """ Create a new object to test the review class """
        self.review = Review()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        """ Testing the creation of attributes of the review class """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')
        self.assertEqual(mock_stdout.getvalue(), '')
        
if __name__ == '__main__':
    """ Run the test """
    unittest.main()
        